from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegistrationForm, AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registration successful. Welcome!")
            return redirect('post_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Login successful. Welcome!")
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})
