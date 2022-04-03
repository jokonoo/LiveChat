from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nickname}'


class UserFavoriteChat(models.Model):
    chat_name = models.CharField(max_length=100)
    user_profile = models.ManyToManyField(
        UserProfile, blank=True, related_name='chats')

    def __str__(self):
        return f'{self.chat_name}'
