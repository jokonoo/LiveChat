from django.contrib import admin
from .models import UserProfile, UserFavoriteChat


admin.site.register(UserProfile)
admin.site.register(UserFavoriteChat)
