# Creative IT Class #10 Topic: Django HttpResponse, Function, url, path Date: 17/05/2023
# Add App path url in the 'main/urls/' file. Example Below:
'''
from django.contrib import admin
from django.urls import path, include <<<<<<<<<<<<<<<<


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myApp.urls'))  <<<<<<<<<<<<<<<<<<
]
'''
# In the "views.py" import HttpResponse and write the function with HttpResponse aand return it
'''
from django.shortcuts import render
from django.http import HttpResponse <<<<<<<<<<<<

# Create your views here.
def index(Request):
    return HttpResponse('<title>Home Page</title><h1>This is My Home page</h1><button><a href="mypage">mypage</a></button')
def mypage(Request):
    return HttpResponse('<title>My Page</title> <h1>This is my second page</h1>')
'''
# Import function and Add route in the "App urls.py"
'''
from django.urls import path
from .views import *    <<<<<<<<<<<<<<<<<<<<

urlpatterns = [
     path('', index, name='home'),  <<<<<<<<<<<<<<<<<
     path('mypage/', mypage, name='mypage') <<<<<<<<<<<<<<

]
'''
# How to Create Run Button in the pycharm IDE and How to show inside of sqlite in the VScode