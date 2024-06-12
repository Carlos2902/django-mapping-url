from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(reques):
    return HttpResponse('Welcome')
def about(reques):
    return HttpResponse('about page')
def menu(reques):
    return HttpResponse('menu page')
def book(reques):
    return HttpResponse('booking page')