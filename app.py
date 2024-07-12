#demo1 for Tau an IVR system 
import os
import requests
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import json


app = Flask(__name__)


#Twilio account credentials 
account_sid= "AC50e46c071290d90aa8e849b63d7a917a"
auth_token = "bc4cfd84c80ef33a82db86b20d61abbd"

#creating the twilio client 
client = Client(account_sid, auth_token)

#updating the webhook url for the phone
phone_number_sid = "PNc41e2f0c589e5726370b22c5a38a13d0"
webhook_url = "/http://127.0.0.1:8000/ivr"

phone_number = client.incoming_phone_numbers(phone_number_sid).fetch()
phone_number.update(voice_url=webhook_url, voice_method='POST')

 # Counter to track the number of interactions
interaction_counter = 0 

 # allowed maximum number of interactions before ending the call
MAX_INTERACTIONS = 3

@app.route('/', methods=['GET'])
def home():
  return "Welcome to Tau's IVR"

@app.route('/ivr', methods=['POST']) 
def handle_ivr():
  global interaction_counter
  response = VoiceResponse()
  response_text = ""

  speech_input = request.values.get('SpeechResult','').lower()

  if 'product' in speech_input:
    response_text = "We are a logistics services company incorporated in Hong Kong, south Africa , Mozambique and Zimbabwe. Our core business is the provision of logistics solutions throughout the world either directly or through strategic alliances.If you are in the market to buy logistics services you have come to the right place. Star International is strategically positioned to provide you with a solution to meet your unique business needs. Visit our website at www.starinternational.co.zw to explore our services."
  elif 'location' in speech_input:
    response_text = "We are located at 96 Willowvale road in Willowvale, Harare."
  elif 'working hours' in speech_input:
    response_text = "Our offices are open from Monday to Saturday, from 8:00 am to 5:00 pm. We're closed on Sundays. But you can talk to me any day"
  else:
   response_text = "I'm sorry, but I couldn't understand your request. Please try again or ask a different question."

#convert text to speech using Twilio's TTS
  response.say(response_text, voice='Ayanda-Neural')
  interaction_counter += 1 

# Checking the maximum number of interactions has been reached 
  if interaction_counter >= MAX_INTERACTIONS:
    response.hangup() 
  else : #Continuing the IVR flow 
    response.gather(input='speech', timeout=3, speechTimeout='auto', action='/ivr')
  return str(response)


if __name__ == '__main__': 
  app.run(port=8000)

