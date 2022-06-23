from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("we are in about")


def contact(request):
    return HttpResponse("we are in contact")


def tracker(request):
    return HttpResponse("we are in tracker")


def search(request):
    return HttpResponse("we are in search")


def productview(request):
    return HttpResponse("we are in productview")


def checkout(request):
    return HttpResponse("we are in checkout")