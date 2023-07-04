from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    context = {}

    # template = loader.get_template("home.html")
    # if template:
    #     return print("ooooooook")
    # return "nonnnn"
    return render(request, "home.html", context)
    # return HttpResponse("Bienvenue à tout le monde")
