from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages  # Import messages framework

def home(request):
    return render(request, 'game/home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('snake')  # Redirect to the game page
        else:
            messages.error(request, "Invalid credentials. Try again!")  # Store error message
            return redirect('login')  # Redirect back to login page to display message

    return render(request, 'game/login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')
    return render(request, 'game/signup.html')

@login_required
def snake_game(request):
    return render(request, 'game/snake.html')

def logout_view(request):
    logout(request)
    return redirect('login')
