from django import forms
from django.forms import fields
from .models import Profile
from django.contrib.auth.models import User

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "bio", ]