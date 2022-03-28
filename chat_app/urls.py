from django.urls import path
from .views import main_view, chat_room

urlpatterns = [
    path('', main_view, name='main'),
    path('<str:room_name>/', chat_room, name='chat_room')
]