from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "local": strftime("%Y-%m-%d %H:%M %p",localtime()),
    }
    return render(request, "index.html", context)

def to_index(request):
    return redirect('/')

# Create your views here.
