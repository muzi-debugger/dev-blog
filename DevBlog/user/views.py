from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('post_list')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render ('home')