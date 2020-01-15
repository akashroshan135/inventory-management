from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),                                              # the 'HomeView' class in the views.py is rendered as view is called when localhost is called
    path('inventory/', views.InventoryListView.as_view(), name = 'inventory'),                      # the 'InventoryListView' class in the views.py is rendered as view is called when localhost is called
    path('inventory/new', views.StockCreateView.as_view(), name = 'new-stock'),                     # the 'StockCreateView' class in the views.py is rendered as view is called when localhost is called
    path('inventory/<pk>/edit', views.StockUpdateView.as_view(), name = 'edit-stock'),              # the 'StockUpdateView' class in the views.py is rendered as view is called when localhost is called
    path('inventory/<pk>/delete', views.StockDeleteView.as_view(), name = 'delete-stock'),          # the 'StockDeleteView' class in the views.py is rendered as view is called when localhost is called
]