from django.shortcuts import render, redirect
from .forms import CustomRegisterForm


def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
    else:
        form = CustomRegisterForm
    return render(request, 'users_app/register.html', {'form': form})
