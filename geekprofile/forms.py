from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nickname = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['username', 'nickname','email', 'password1', 'password2']

#this inherits from UserCreationForm and adds the email fields
