# Official Python base image
FROM python:3.12.4

# Setting the working directory in the container
WORKDIR /app

# Copying the requirements file to the container
COPY requirements.txt .

# Installing the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

#  Port on which the Flask app will run
EXPOSE 5000

#Command to run the Flask app
CMD ["python3", "app.py"]