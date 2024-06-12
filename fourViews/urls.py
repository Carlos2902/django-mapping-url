from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name = 'home' ),
    path('aboutus/', views.about, name = 'about us' ),
    path('menu/', views.menu, name = 'menu' ),
    path('book/', views.book, name = 'booking' ),
]