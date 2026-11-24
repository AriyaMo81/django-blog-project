from django.shortcuts import render, redirect
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib import messages


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
