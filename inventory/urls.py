from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),                                              # the 'HomeView' class in the views.py is rendered as view is called when localhost is called
    path('inventory/', views.InventoryListView.as_view(), name = 'inventory'),                      # the 'InventoryListView' class in the views.py is rendered as view is called when localhost is called
    path('inventory/new-stock', views.StockCreateView.as_view(), name = 'new-stock'),               # the 'StockCreateView' class in the views.py is rendered as view is called when localhost is called
]