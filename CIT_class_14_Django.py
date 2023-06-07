# Creative IT Class #14 Topic: Create Data with Message into Database and Nav bar Design Date: 31/05/2023
# How to Create Data(User Information) into database. Example Below:

# In the HTML Form:
'''
<div class="container">
        <div class="row">
            <div class="col-lg-4">
                <form method="POST" enctype="multipart/form-data">
                    {% csrf_token %}
                    <div class="form-group">
                        <label>name</label>
                        <input type="text" name="name" class="form-control" placeholder="Enter Name">
                        <br>
                        <label>Email address</label>
                        <input type="email" name="email" class="form-control" placeholder="Enter email">
                        <br>
                        <label>Phone</label>
                        <input type="text" name="phone" class="form-control" placeholder="Enter Phone">
                        <br>
                        <label>Age</label>
                        <input type="text" name="age" class="form-control" placeholder="Enter Age">
                        <br>
                        <label>Address</label>
                        <input type="text" name="address" class="form-control" placeholder="Enter Address">
                        <br>
                        <label>Date of Birth</label>
                        <input type="datetime-local" name="dob" class="form-control" placeholder="Enter Date of Birth">
                        <br>
                        <label>Image</label>
                        <input type="file" name="image" class="form-control" placeholder="Upload Image">
                        <img src="" alt="">
                        <br>
                        <label>Religion</label>
                        <select name="religion" class="custom-select">
                        <option selected>Please select religion</option>
                        <option value="Islam">Islam</option>
                        <option value="Hinduism">Hinduism</option>
                        <option value="Buddhism">Buddhism</option>
                        <option value="Judaism">Judaism</option>
                        <option value="Christianity">Christianity</option>
                        </select>
                        <br><br>
                        <label>Gender</label>
                        <select name="gender" class="custom-select">
                        <option selected>Please select gender</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Others">Others</option>
                        </select>
                    </div>
                    <br>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </div>
'''
# In the Views.py
'''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile

def create(Request):
    if Request.method == 'POST':
        name     = Request.POST.get('name')
        image    = Request.FILES.get('image')
        email    = Request.POST.get('email')
        age      = Request.POST.get('age')
        address  = Request.POST.get('address')
        phone    = Request.POST.get('phone')
        dob      = Request.POST.get('dob')
        religion = Request.POST.get('religion')
        gender   = Request.POST.get('gender')

        if name:
            if image:
                prof = Profile.objects.create(
                    name     = name,
                    image    = image,
                    email    = email,
                    age      = age,
                    address  = address,
                    phone    = phone,
                    dob      = dob,
                    religion = religion,
                    gender   = gender
                )
                prof.save()
                messages.success(Request, 'User Account has been Created successfully')
                return redirect('main')
            else:
                prof = Profile.objects.create(
                    name        = name,
                    email       = email,
                    age         = age,
                    address     = address,
                    phone       = phone,
                    dob         = dob,
                    religion    = religion,
                    gender      = gender
                )
                prof.save()
                messages.success(Request, 'User Account has been Created successfully without user image')
                return redirect('main')
        else:
            messages.error(Request, "Please Fill up all fields.")
    return render(Request, 'create.html', locals())
'''
# In the urls.py
'''
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create')
]
'''
# Show Message in the HTML file. Example Below:
'''
{% if messages %}
    <ul class="messages">
        {% for message in messages %}
            <li {% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
        {% endfor %}
    </ul>
{% endif %}
'''
# How to assign url link in the HTML file. Example Below:
'''
<ul class="navbar-nav mr-auto">
    <li class="nav-item">
        <a class="nav-link" href="{% url 'create' %}">Add User</a>
    </li>
</ul>
'''
# How to use f-string for retribe multiple data from database. Example Below:
'''
    def __str__(self):
        return f'{self.name} - {self.email}'

'''
# How to Copy image path from pycharm. Example Below:
'''
step_1: right click on image from media/image_forlder
step_2: Go to "Copy Relative Path" in the menu 
'''
