from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user']

