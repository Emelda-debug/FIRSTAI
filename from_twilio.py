from twilio.rest import Client

# Twilio account credentials
account_sid = "AC50e46c071290d90aa8e849b63d7a917a"
auth_token = "828a6679569331e77ca6b4e9dfca3d66"

# Create a Twilio client
client = Client(account_sid, auth_token)

# Search for the phone number by its number
phone_number = '+19126122534' 

numbers = client.incoming_phone_numbers.list(phone_number=phone_number)

if numbers:
    phone_number_sid = numbers[0].sid
    print(f"The Phone Number SID for {phone_number} is: {phone_number_sid}")
else:
    print("Phone number not found in the Twilio account.")