# Use an official Python runtime as a base image
FROM python:3.7-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run gunicorn when the container launches
CMD gunicorn -w 4 app:app -b 0.0.0.0:80
