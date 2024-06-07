from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def menu(request, dish):
    items = {
        'pasta': 'lorem ipsum',
        'cheescake': 'lorem ipsum',
        'falafael': 'lorem ipsum',
    }
    description = items[dish]
    return HttpResponse(f'Dish selected: <h2>{dish}</h2> <br> <h4>description: </h4> {description}')