# Creative IT Class #09 Topic: Django Super user password and App creation Date: 15/05/2023
# Django Virtual Environment create: CMD Command>>> python -m venv env
# Django Activate Environment: CMD Command>>> env\Scripts\activate
# Install pip: CMD Command>>> pip install django
# Django Create Project with "Manage.py": CMD Command>>> django-admin startproject project_name .
# Django Create Admin and Run Server: CMD Command>>> python manage.py runserver
# Brows the url: 127.0.0.1:8000
# To freeze server >>> pip freeze
# To migrate table in database >> python manage.py makemigrations
# To run migration >> python manage.py migrate
# Go to admin panel >> http://127.0.0.1:8000/admin/login/?next=/admin/
# To Create user >> python manage.py createsuperuser
# Enter your user name
# Enter your email
# Enter your password
# Confirm your password
# To Create your App >> python manage.py startapp App_Name
# To Add App in the settings.py file. Example Below:
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App', <<<<<<<<<<<<<<<<<
]
'''
# Copy urls.py from 'main' project folder and past to root of 'App' folder
# Add App path url in the 'main/urls/' file. Example Below:
'''
from django.contrib import admin
from django.urls import path, include <<<<<<<<<<<<<<<<


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myApp',include('myApp.urls'))  <<<<<<<<<<<<<<<<<<
]
'''
# Change in the 'App/urls' file. Example Below:
'''
from django.urls import path

urlpatterns = [
    path()
]
'''
# SQL lite viewer web App url: https://sqliteviewer.app/
# Go to above mention URL and Brows 'db.sqlite3' file from your project folder
# Now you can get all the database tables and records

