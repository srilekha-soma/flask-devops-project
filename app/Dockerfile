# Dockerfile is a script that tells Docker how to build a container image for your Flask app.

# Use official Python image
# a lightweight version of Python 3.9 called slim, which includes only essential libraries. 
# This keeps your container small and fast.
FROM python:3.9-slim

# Set working directory
# This creates (or switches to) the /app folder inside the container.
# Any commands after this will run inside that folder.
WORKDIR /app

# Copy files and install dependencies
# This copies your requirements.txt file from your project folder (on your computer) into the container’s /app directory.
COPY requirements.txt .

# This installs your Python dependencies (like Flask and Werkzeug) inside the container using pip.
RUN pip install -r requirements.txt

# This copies the rest of your app files (like app.py) into the container’s /app directory.
COPY . .

# Expose port and run the app
# This tells Docker that your app will use port 5000 (Flask’s default).
EXPOSE 5000

# This is the default command Docker runs when you start the container.
CMD ["python", "app.py"]
