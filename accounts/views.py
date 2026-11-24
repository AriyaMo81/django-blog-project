from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserloginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def create_user(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            user = User.objects.create_user(
                username=cd["username"],
                email=cd["email"],
                password=cd["password"]
            )

            user.first_name = cd["firstname"]
            user.last_name = cd["lastname"]
            user.save()

            messages.success(request, "User created successfully!")

            return redirect("home")

    else:
        form = UserCreateForm()

    return render(request, "user_create.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = UserloginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "User logged in successfully!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
                return redirect("login_user")
    else:
        form = UserloginForm()
        return render(request, "user_login.html", {"form": form})
