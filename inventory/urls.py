from django.urls import path
from django.conf.urls import url
from django_filters.views import FilterView
from .filters import StockFilter
from . import views

urlpatterns = [
    path('', FilterView.as_view(filterset_class=StockFilter, 
        template_name='inventory.html'), name='inventory'),
    path('new', views.StockCreateView.as_view(), name = 'new-stock'),
    path('stock/<pk>/edit', views.StockUpdateView.as_view(), name = 'edit-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name = 'delete-stock'),
]