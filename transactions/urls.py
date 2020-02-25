from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers-list'),
    path('suppliers/new', views.SupplierCreateView.as_view(), name='new-supplier'),
    path('suppliers/<pk>/edit', views.SupplierUpdateView.as_view(), name='edit-supplier'),
    path('suppliers/<pk>/delete', views.SupplierDeleteView.as_view(), name='delete-supplier'),
    path('suppliers/<name>', views.SupplierView.as_view(), name='supplier'),

    path('purchases/', views.PurchaseView.as_view(), name='purchases-list'), 
    path('purchases/new', views.SelectSupplierView.as_view(), name='select-supplier'), 
    path('purchases/new/<pk>', views.PurchaseCreateView.as_view(), name='new-purchase'),    
    path('purchases/<pk>/delete', views.PurchaseDeleteView.as_view(), name='delete-purchase'),
    
    path('sales/', views.SaleView.as_view(), name='sales-list'),
    path('sales/new', views.SaleCreateView.as_view(), name='new-sale'),
    path('sales/<pk>/delete', views.SaleDeleteView.as_view(), name='delete-sale'),

    path("purchases/<billno>", views.PurchaseBillView.as_view(), name="purchase-bill"),
    path("sales/<billno>", views.SaleBillView.as_view(), name="sale-bill"),
]