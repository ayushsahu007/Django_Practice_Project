from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(request.POST)
        print(email)
            #cheak duplicate username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")
          
          # duplicate Email 
        if User.objects.filter(email=email).exists():
           messages.error(request, "Email already exists.")
           return redirect("register")
       
               # Allowed email domains
        allowed = ["gmail.com", "yahoo.com", "outlook.com"]

        domain = email.split("@")[-1]

        if domain not in allowed:
            messages.error(request, "Email provider is not allowed.")
            return redirect("register")

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email = email,
            username=username,
            password=password
        )

        messages.success(request, "Account created successfully.")
        return redirect("login")

    return render(request, "register.html")


def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

        login(request, user)
        return redirect("receipes")

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("login")