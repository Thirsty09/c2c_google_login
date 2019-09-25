# Application walkthrough

## Google Authentication:
Simple Google Authentication app in Django with the  all-auth app library

### Introduction:
This walkthrough shows a simple way to setup google authentication in Django using the all-auth library.

### Requirements:
* Python3
* Django
* django-allauth

### Running the Application:
* Make sure all requirements are installed.
* Create the main project directory.
* Create a Virtual Environment in the shell, if there is not an existing one.
* Create a new Django Project if there is not an existing one [django-admin startproject myprojectname].
* Change the path to the project directory [cd myprojectname].
* Clone/Download the repository and place in the project directory OR use it as a guide to create your app.
* Make migration [python manage.py migrate].
* Create a superuser for administrative purposes.
* Run the Server [python manage.py runserver].
* Open your Browser and run http://localhost:8000/admin or http://127.0.0.1:8000/admin.
* Choose your social login provider.
* Set your client key and secret key.
* Change the server IP from 'example.com' to 'localhost:8000' or '127.0.0.1:8000'.
* Exit admin and run the app on the server.
* Login.

### NOTE:
* You can get your unique CLient and Secret key from https://console.developers.google.com.
