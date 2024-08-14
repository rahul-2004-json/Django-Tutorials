from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    # return HttpResponse("You are at home page")
    return render(request,"website/index.html")

def about(request):
    return HttpResponse("You are at about page")

def contact(request):
    return HttpResponse("You are at contact page")