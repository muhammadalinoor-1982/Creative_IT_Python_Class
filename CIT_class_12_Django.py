# Creative IT Class #12 Topic: Django Table Creation and Migration Date: 24/05/2023
# Before Creating a Table, install "pillow" Command: python -m pip install pillow
# Install pillow for Image Field in the Table
# Go to App/models.py for table creation. Example Below:
'''
class Profile(models.Model):

    RELIGION = (
        ('Islam','Islam'),
        ('Hinduism','Hinduism'),
        ('Buddhism','Buddhism'),
        ('Judaism','Judaism'),
        ('Christianity','Christianity')
    )

    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )

    name        =     models.CharField  (max_length=30, null=True, blank=True)
    image       =     models.ImageField (upload_to='pro_pic/', default='default/no_img.jpg', null=True, blank=True)
    email       =     models.EmailField (max_length=30, null=True, blank=True)
    age         =     models.PositiveIntegerField(null=True, blank=True)
    address     =     models.TextField  (max_length=300, null=True, blank=True)
    phone       =     models.TextField  (max_length=15, null=True, blank=True)
    dob         =     models.TextField  (max_length=12, null=True, blank=True)
    religion    =     models.CharField  (max_length=20, choices=RELIGION)
    gender      =     models.CharField  (max_length=10, choices=GENDER)

'''
# Need to execute migration: Command>>> python manage.py makemigrations
# Now Migrate: Command>>> python manage.py migrate

# Register Table in the App/admin.py file. Example Below:
'''
from django.contrib import admin
from .models import *   <<<<<<<<<<<<<<

# Register your models here.
admin.site.register(Profile)   <<<<<<<<<<<<

# Here "Profile" is Table name
'''
# IF Need to show profile list by Name, then go to "App/models.py" then write a function bottom of the file. Example Below:
'''
    def __str__(self):
        return str(self.name)
''' 
# Auto Create Media Folder in the root directory to contain Image files.
# In the Tabile field: image = models.ImageField (upload_to='pro_pic/')
# It will Effect on "project/urls.py". Example Below:
'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  <<<<<<<<<<
'''
# Need to Create default image folder Manually.
# image = models.ImageField (upload_to='pro_pic/', default='default/no_img.jpg')
# Go to Media Folder in the root directory and create another folder named "default" and put an Image call "no_img.jpg"
