from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1> Hey welcome to accounts </h1>")

def signup(request):
    return HttpResponse("<h1> Hey Signup </h1>")

def login(request):
    return HttpResponse("<h1> Hey login </h1>")
