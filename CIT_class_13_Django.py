# Creative IT Class #13 Topic: Read Data from Database and Design Form for Create Data Date: 29/05/2023
# How to Include CSS ans JS File in the HTML Template. Example Below:
'''
<!DOCTYPE html>
<html lang="en">
{% load static %}  <<<<<<<<<<<<<<
<head>
    <meta charset="UTF-8">
    <title>{% block title %}First{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/min.css' %}">   <<<<<<<<<<<<<<<<<<
    <script src="{% static 'js/min.js' %}"></script>        <<<<<<<<<<<<<<<<<<
</head>
'''
# How to Extends Master HTML File into Slave HTML File. Example Below:
'''
# This HTML File Name is create.html

{% extends 'First.html' %}  <<<<<<<<<<<<<<<<<<
{% block title %}Create Page{% endblock %}  <<<<<<<<<<<<<<<<<<
{% block body %}  <<<<<<<<<<<<<<<<<<
<div class="container">
<p>Hellow</p>
</div>
{% endblock %}  <<<<<<<<<<<<<<<<<<
'''
# How to Reade Database Contant in the Browser. Example Below:

# In the Views.py
'''
from .models import Profile     #Table Name is "Profile"

def main(Request):
    user_prof = Profile.objects.all()
    return render(Request,'First.html', locals())
'''
# In the urls.py
'''
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
]
'''
# In the HTML File
'''
{% block body %}
    <div class="container">
        <div class="row">
            {% for i in user_prof %}  <<<<<<<<<<<<
                <div class="col-lg-3">
                    <div class="card text-white bg-dark mb-3" style="max-width: 18rem;">
                        <div class="card-header">{{ i.name }}</div>   <<<<<<<<<<<<<<<<<<<<<<
                        <img class="card-img-top" src="{{ i.image.url }}" alt="Card image cap">  <<<<<<<<<<<
                        <div class="card-body">
                            <h5 class="card-title">{{ i.email }}</h5>  <<<<<<<<<<<<<<
                            <p class="card-text">{{ i.address }}</p>   <<<<<<<<<<<<<<<<<<
                            <a href="#" class="btn btn-primary">Go somewhere</a>
                        </div>
                    </div>
                </div>
            {% endfor %}   <<<<<<<<<<<<<<<<
        </div>
    </div>
    {% endblock %}
'''
# ____________________________________________________________________
