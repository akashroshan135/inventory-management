from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),    # the 'home' function in the views.py is called when localhost is called
]