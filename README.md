    URL Shortener Project

# Project Description

The URL Shortener project is a web application built with Django that allows users to shorten long URLs, making them easier to share. The application provides a simple interface for users to input their long URLs and get a shortened version. Users can also view a list of their shortened URLs and delete them if needed.

# Features

Shorten long URLs to a 6-character code. Redirect to the original URL when the short code is accessed. Display a list of all shortened URLs. Delete shortened URLs. Responsive design using Bootstrap for styling.

#Steps to configure and run the Django project.

1]You can activate virtual environment :
  cd venv/scripts
  activate
  cd..   -to go back to urlshortener directory

   or
  
  Install the dependencies: 
  pip install -r requirements.txt

2]Apply migrations: 
  python manage.py makemigrations 
  python manage.py migrate

3]Run the development server: 
  python manage.py runserver

4]Open your web browser and navigate to http://localhost:8000.

# Description
urlshortener/: The root directory of the Django project.

Dockerfile: The Dockerfile used to build the Docker image for the project.
docker-compose.yml: The Docker Compose file to define and run multi-container Docker applications.
manage.py: The command-line utility that lets you interact with this Django project.
shortener/: The main application directory containing the URL shortener app.

forms.py: Contains the form classes used in the application.

models.py: Contains the data models for the application.

templates/: Directory for storing HTML template files.

shortener/: Subdirectory for the shortener app's templates.
home.html: The main template for the URL shortener application.
urls.py: Contains the URL declarations for the shortener app.

views.py: Contains the view functions for the application.

static/: Directory for storing static files such as CSS and JavaScript.

css/: Directory for storing CSS files.
style.css: Custom CSS styles for the application.
urlshortener/: The main project directory containing the project settings and configurations.

settings.py: Configuration file for the Django project.
urls.py: The main URL configuration file for the Django project. 
requirements.txt: A file listing the Python dependencies needed to run the project.

# Backend Schema
The backend schema consists of a single model that handles the storage and management of URLs. Below is the detailed description of the model used in this project.

URL Model
The URL model is designed to store the original URLs along with their corresponding shortened codes. It includes the following fields:

original_url: A URLField to store the original long URL.
short_code: A CharField to store the unique 6-character shortened code. This code is generated using a helper function.
created_at: A DateTimeField to store the timestamp when the URL was created.

# Flowchart
  Flowchart png image in urlshortenet directory

# Instructions for building and running the Docker container.

1] Build the Docker Image:
docker build -t urlshortener:latest .

2] Run the Docker Container:
docker run -d -p 8000:8000 urlshortener:latest

3] Access the Application:
http://localhost:8000


# Using Docker Compose

1] Build and Start the Containers:
docker-compose up --build

2] Access the Application:
http://localhost:8000
