from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('purchases/', views.PurchaseView.as_view(), name = 'purchases'), 
    path('purchases/new', views.SelectSupplierView.as_view(), name = 'select-supplier'), 
    path('purchases/new/<pk>', views.PurchaseCreateView.as_view(), name = 'new-purchase'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers-list'),
    path('suppliers/new', views.SupplierCreateView.as_view(), name='new-supplier'),
    path('suppliers/<pk>/edit', views.SupplierUpdateView.as_view(), name='edit-supplier'),
    path('suppliers/<name>', views.SupplierView.as_view(), name='supplier'),
]