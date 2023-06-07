# Creative IT Class #15 Topic: Search and Delete Operation Date: 05/06/2023
# Search Operation

# In HTML File
'''
<form class="form-inline my-2 my-lg-0" method="GET">
    <input class="form-control mr-sm-2" type="text" name="search" placeholder="Search" aria-label="Search">
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
</form>
'''
#  In view File
'''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import Profile

# Create your views here.
def main(Request):
    if Request.method == 'GET':
        search = Request.GET.get('search')
        if search:
            user_prof = Profile.objects.filter(
                Q(name__icontains=search) |
                Q(email__icontains=search) |
                Q(age__icontains=search) |
                Q(religion__icontains=search)
            )
            if not user_prof:
                messages.warning(Request, 'No such Account Exist')
                return redirect('main')
        else:
            user_prof = Profile.objects.all()
    return render(Request,'First.html', locals())
'''
# Delete Operation

# In the urls.py
'''
path('delete/<int:id>/', delete, name='delete')
'''
# In the Views.py
'''
def delete(Request, id):
    prof = Profile.objects.get(id=id)
    prof.delete()
    messages.error(Request, 'Profile has been deleted successfully')
    return redirect(main)
''' 
# In the HTML File
'''
<a href="{% url 'delete' i.id %}" class="btn btn-danger">Delete</a>
'''
