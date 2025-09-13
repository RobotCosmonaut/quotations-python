#   CS 7319 Software Architecture
#   Homework 4
#   Kubernetes Hands-On – Minikube Deployment
#   Ron Denny
#   rdenny@smu.edu
#
#   Note: this is based on the Demo Docker file noted for Homework 1B

#Use a lightweight official Python image as the base
FROM python:3.9-slim

#Set the working directory inside the container
WORKDIR /app

#Copy the requirements file and install the dependencies
#This is done first to leverage Docker's build cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy all the application files into the container
COPY . .

#Expose the port the app runs on
EXPOSE 8080

#Define the command to run the application when the container starts
#The host must be set to 0.0.0.0 to be accessible outside the container
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
