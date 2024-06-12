from django.urls import path, include
from . import views


urlpatterns = [
    path('menu/<str:dish>', views.menu, name = 'menu'),
]