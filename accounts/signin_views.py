from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request, "Auth failed")            
    return render(request, './accounts/signin.html')

def logout_user(request):
    logout(request)
    messages.info(request, "Logged Out Successfully")
    return redirect('/')