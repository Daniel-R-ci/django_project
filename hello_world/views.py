from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.method=="GET":
        return HttpResponse(request.method)
    elif request.method=="POST":
        HttpResponse("You must have POSTed something!")
