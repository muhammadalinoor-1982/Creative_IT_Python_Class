# Creative IT Class #17 Topic: Profile Details and Update Page Templating Date: 14/06/2023
# Create detailsProfile.html then templating and push python code to get profile data fom database.

# In the views.py
'''
# For Profile Details
def detailsProfile(Request, id):
    prof = Profile.objects.get(id=id)
    return render(Request,'detailsProfile.html', locals())

    # For Profile Update page
def update(Request, id):
    prof = Profile.objects.get(id=id)
    return render(Request, 'update.html', locals())
'''

# In the urls.py
'''
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('detailsProfile/<int:id>/', detailsProfile, name='detailsProfile'),  <<<<<<<<<< 
    path('update/<int:id>/', update, name='update')   <<<<<<<<<<
]

'''