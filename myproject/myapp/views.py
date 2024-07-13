from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Little Lemon restaurant! Hello Customer!")

def menu(request):
    return HttpResponse("This is the Menu")

def display_date(request):
    return HttpResponse(datetime.today())