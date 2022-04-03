from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, UserFavoriteChat


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['user', 'chats']


class ChatForm(forms.ModelForm):

    class Meta:
        model = UserFavoriteChat
        fields = ['chat_name']
