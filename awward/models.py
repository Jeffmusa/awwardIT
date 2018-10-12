from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =30,null=True)
    pro_photo = models.ImageField(upload_to = 'images/',null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    

class Projects(models.Model):
    name = models.CharField(max_length =30,null=True)
    screenshot = models.ImageField(upload_to = 'images/',null=True)
    description = models.TextField(null=True)
    link = HTMLField()
    user = models.ForeignKey(User, null=True)