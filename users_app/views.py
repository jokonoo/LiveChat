from django.shortcuts import render, redirect
from .forms import CustomRegisterForm, ProfileForm, ChatForm
from .models import UserProfile


def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat_main')
    form = CustomRegisterForm
    return render(request, 'users_app/register.html', {'form': form})


def profile_view(request):
    chats = UserProfile.objects.get(user=request.user).chats.all()
    if request.method == 'POST':
        form_p = ProfileForm(request.POST, instance=request.user.userprofile)
        form_c = ChatForm(request.POST)
        if form_p.is_valid() and form_c.is_valid():
            form_p.save()
            new_chat = form_c.save()
            new_chat.user_profile.add(UserProfile.objects.get(user=request.user))
            return redirect('profile')
    form_p = ProfileForm(instance=request.user.userprofile)
    form_c = ChatForm()
    return render(request, 'users_app/profile.html', {'form_p': form_p, 'form_c': form_c, 'chats': chats})

