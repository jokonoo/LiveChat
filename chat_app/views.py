from django.shortcuts import render


def main_view(request):
    return render(request, 'chat_app/chat_main.html')


def chat_room(request, room_name):
    return render(request, 'chat_app/chat_room.html', {'room_name': room_name})
