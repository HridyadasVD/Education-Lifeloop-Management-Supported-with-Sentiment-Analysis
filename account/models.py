from django.db import models
from django.contrib.auth.models import User
import os

from django.db.models.deletion import CASCADE
# Create your models here.

def path_and_rename(instance,filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    #get filename 
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username,ext)
    return os.path.join(upload_to,filename)


class User_Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150,blank=True)
    profile_pic = models.ImageField(upload_to = path_and_rename,verbose_name='Profile Picture', blank=True)

    teacher = 'teacher'
    student = 'student'
    
    user_types = [
        (teacher,'teacher'),
        (student,'student'),
        
    ]
    user_type = models.CharField(max_length=10,choices=user_types,default=student)

    def __str__(self):
        return self.user.username


class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    content = models.TextField()

    def _str_(self):
        return self.name

class StudentReview(models.Model):
    student=models.CharField(max_length=100)
    review=models.TextField(max_length=500)
    value=models.TextField(max_length=250)
    def _str_(self):
        return self.student