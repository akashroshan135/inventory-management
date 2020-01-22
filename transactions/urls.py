from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('purchases/', views.PurchaseView.as_view(), name = 'purchases'), 
    path('purchases/new', views.PurchaseCreateView.as_view(), name = 'new-purchase'), 
]