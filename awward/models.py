from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    pro_photo = models.ImageField(upload_to = 'images/',null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    
    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length =30,null=True)
    screenshot = models.ImageField(upload_to = 'images/',null=True)
    description = models.TextField(null=True)
    link = models.URLField()
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.CharField(max_length =80,null=True)
    user = models.ForeignKey(User,null=True)
    project = models.ForeignKey(Projects,related_name='comments',null=True)

    def __str__(self):
        return self.comment