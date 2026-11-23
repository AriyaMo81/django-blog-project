from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.


def home(request):
    todos = Todo.objects.all()
    return render(request, "home.html", {"todos": todos})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, "detail.html", {"todo": todo})
