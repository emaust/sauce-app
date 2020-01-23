# sauce-app

SauceProtecc has been created for the purpose of assisting individuals in monitoring the use of their original content online.


## Installation and Set Up
SauceProtecc relies on the Google Cloud Vision API. To utilitze the API, use the following steps:
1. Create a Google Cloud account at https://cloud.google.com/
2. Download the Google Cloud Vision Library for Python within a virtual env
    - https://cloud.google.com/vision/docs/libraries#client-libraries-install-python
    - https://googleapis.dev/python/vision/latest/index.html
    - https://virtualenv.pypa.io/en/latest/
3. Follow the documentation provided to register a user, application, and download a Google credential key for a Google Could Vision account. This is not the same as an API key, and will be a json file that will be added to the django settings.py file.
    - https://cloud.google.com/vision/docs/before-you-begin
4. Create a .env file within your outermost application file creating an environment variable for the Google credentials.
5. Follow the documentation for applying the code in the django file. This application utilizes the web detection API, and alters the annotation method provided by Google to produce a list of website results. 

This application does not use the SQLite database provided by Django, and was created using Django with a Postgres database. Postgres was downloaded using Homebrew. In order for Django to access your database, the following steps should be taken:

 1. Create a Postgres database using psql and the CREATE DATABASE <your-database-name>
 2. Write import dj_database_url at the top of the settings.py file
 3. Change the settings for the database from the default for SQLite to the following:
 
    if os.environ.get("ENVIRONMENT") == "PROD":
      DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}

    else:
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': os.environ.get('DB_NAME'),
              'USER': os.environ.get("DB_USER"),
              'PASSWORD': os.environ.get("DB_PASS"),
              'HOST': "localhost",
              'PORT': "5432",
          }
      }

   
A requirements.txt file has been provided that provides a full list of dependencies. The file was created by running $ pip freeze > requirements.txt within the main app with the virtualenv active.


## Creating Environment Variables
The following variables should be included in the .env file in order to properly connect Django to a Postgres database, hide the secret key provided by Django, and to hide the Google credential json file. In order for Django to access the environment variables, be sure to enter the following into your settings.py:

from dotenv import load_dotenv
load_dotenv()
import os


The .env file should be included in the .gitignore file. The following variables should be set and exported for use in the settings.py file:
    - DB_NAME sets the Postgres database name
    - DB_USER sets the expected user for that database
    - DB_PASS is the password used to access the database
    - GOOGLE_APPLICATION_CREDENTIALS provides the local path to the .json file provided by Google for use of the Cloud Vision products
    - SECRET_KEY should contain the secret key provided by Django in the settings.py file.

## Deployment
This app was deployed to Heroku, which required the creation of a Procfile to declare its process types.



