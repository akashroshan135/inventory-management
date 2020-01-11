from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),                                        # the 'home' function in the views.py is called when localhost is called
    path('inventory/', views.inventory, name = 'inventory'),                    # the 'inventory' function in the views.py is called when localhost is called
    path('inventory/new-stock', views.new_stock, name = 'new-stock'),           # the 'new_stock' function in the views.py is called when localhost is called
]