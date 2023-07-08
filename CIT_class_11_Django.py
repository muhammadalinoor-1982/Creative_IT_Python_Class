# Creative IT Class #11 Topic: Django Templateing and Static Date: 22/05/2023
# Create a folder in the root directory of the project: Folder Name: "template"
# Then Create a HTML file in the "template" folder
# Assign "template" in the setting file of the "template" portion. Example below:
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'], <<<<<<<<<<<<<<<<
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
''' 
# Create a folder in the root directory of the project: Folder Name: "static"
# Configure "static" in the setting file of the "static" portion. Example below:
# Static Directory use for Media files Example: CSS, JavaScript, Images etc
'''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'                      |<<<<<<<<<<
MEDIA_URL = 'media/'                        |<<<<<<<<<<
STATICFILES_DIRS = [BASE_DIR / 'static', ]  |<<<<<<<<<<
MEDIA_ROOT = BASE_DIR / 'media'             |<<<<<<<<<<
'''  
# Then Configure "static" to the "project" urls.py file.Example below:
'''
from django.conf import settings  <<<<<<<<<<<<<<<<<<
from django.conf.urls.static import static  <<<<<<<<<<<<<<<<

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls'))
]

if settings.DEBUG:  <<<<<<<<<<<<<<<
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  <<<<<<<<<<<<<
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  <<<<<<<<<<<<<<<<<<<<

'''
# Execute HTML file in the browser from "views.py". Example below:

# views.py file
'''
from django.shortcuts import render
from django.http import HttpResponse

def main(Request):
    return render(Request,'First.html')  <<<<<<<<<<
'''
# In the App folder: urls.py file
'''
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
]

'''
# Take input using "form" with GET.get method. Example below:

# views.py file
'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(Request):
    value = Request.GET.get('txt')  <<<<<<<<<<<<<<
    return render(Request,'First.html')  
'''
# In the HTML file
'''
    <form>
        <input type="text" name="txt">
        <input type="submit" value="submit">
    </form>
'''
# Note: After submit value using html form by presing submit button, output will show in the browser url.Example below:
# output: http://127.0.0.1:8000/?txt=result here value of "name" field is "?txt=result"

# Take input using "form" with POST.get method, CSRF Token and "locals()". Example below:

# views.py file
'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(Request):
    value = Request.POST.get('txt')  <<<<<<<<<<<<<<<<
    return render(Request,'First.html', locals())  <<<<<<<<<<<<<<<<<
'''
# In the HTML file
'''
    <form method="POST">  <<<<<<<<<<<<<
        {% csrf_token %}  <<<<<<<<<<<<<
        <input type="text" name="txt">
        <input type="submit" value="submit">
    </form>
    <p>Input value is: {{value}}</p>   <<<<<<<<<<<<<<
'''
# Take input using "form" with POST.get method, CSRF Token and "context". Example below:

# views.py file
'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(Request):
    value = Request.POST.get('txt')
    context = {         <<<<<<<<<<<<<<<<<<
        'data' : value  <<<<<<<<<<<<<<<<<<
    }                   <<<<<<<<<<<<<<<<<<
    return render(Request,'First.html', context)  <<<<<<<<<<<<<<<
'''
# In the HTML file
'''
    <form method="POST">  
        {% csrf_token %}  
        <input type="text" name="txt">
        <input type="submit" value="submit">
    </form>
    <p>Input value is: {{data}}</p>   <<<<<<<<<<<<<<
'''
# ________________________________________________________________________

# Some Notes:

# How to assign "csrf tiken" ? Example: {% csrf_token %}
# How to fetch value from python object to html tag ? Example: <p>Input value is: {{data}} </p>
# Capital "GET" use to fetch data from HTML file
# Small "get" use to fetch data from Database

# If need to change "template" directory out of conventional approch then what to do ? Example below:
# Import os in the top of the "settings.py" file
# Then go to "template" portion of the "settings.py" file
# then use: >>>>> 'DIRS': [os.path.join(BASE_DIR, 'template')],

# Notes about "DEBUG"
# If need to off error reporting, specially when project goes live ?
# Go to settings.py file then change value of "DEBUG". Example: DEBUG = False
# Then Change in the "ALLOWED_HOSTS = []". Example: ALLOWED_HOSTS = ['*']

