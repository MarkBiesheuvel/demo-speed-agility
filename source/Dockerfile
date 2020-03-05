# Use an official Python runtime as a base image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt only for improved layer caching
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at working directory
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run gunicorn when the container launches
CMD gunicorn -w 4 app:app -b 0.0.0.0:80
