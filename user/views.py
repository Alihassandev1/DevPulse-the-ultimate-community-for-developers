# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib import messages

# app_name = "user"

# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("home")
#         else:
#             msg = "Invalid username or password"
#             messages.error(request, msg)
#     return render(request, "user/login.html")

# def user_signup(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
#         if user is not None:
#             login(request, user)
#             msg = "User created successfully"
#             messages.success(request, msg)
#             return redirect("home")
#         else:
#             msg = "User not created"
#             messages.error(request, msg)
#     return render(request, "user/login.html")

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import SignupForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    form = SignupForm()
    return render(request, 'user/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')

