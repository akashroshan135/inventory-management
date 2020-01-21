from django.urls import path
from django.conf.urls import url
from django_filters.views import FilterView
from .filters import StockFilter
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),                                              # the 'HomeView' class in the views.py is rendered as view is called when localhost is called
    path('inventory/', FilterView.as_view(filterset_class=StockFilter, 
        template_name='inventory.html'), name='inventory'),                                         # the 'FilterView' class from the django-filters app is rendered as view using the inventory template when localhost is called
    path('inventory/new', views.StockCreateView.as_view(), name = 'new-stock'),                     # the 'StockCreateView' class in the views.py is rendered as view is called when localhost is called
    path('inventory/<pk>/edit', views.StockUpdateView.as_view(), name = 'edit-stock'),              # the 'StockUpdateView' class in the views.py is rendered as view is called when localhost is called
    path('inventory/<pk>/delete', views.StockDeleteView.as_view(), name = 'delete-stock'),          # the 'StockDeleteView' class in the views.py is rendered as view is called when localhost is called
]