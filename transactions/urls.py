from django.urls import path
from django.conf.urls import url
from django_filters.views import FilterView
from .filters import SaleFilter
from .models import SaleBill
from . import views

urlpatterns = [
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers-list'),
    path('suppliers/new', views.SupplierCreateView.as_view(), name='new-supplier'),
    path('suppliers/<pk>/edit', views.SupplierUpdateView.as_view(), name='edit-supplier'),
    path('suppliers/<name>', views.SupplierView.as_view(), name='supplier'),

    path('purchases/', views.PurchaseView.as_view(), name='purchases-list'), 
    path('purchases/new', views.SelectSupplierView.as_view(), name='select-supplier'), 
    path('purchases/new/<pk>', views.PurchaseCreateView.as_view(), name='new-purchase'),    

    path('sales/', FilterView.as_view(filterset_class=SaleFilter, queryset=SaleBill.objects.order_by('-time'),
        template_name='sales/sales_list.html'), name='sales-list'),
    path('sales/new', views.SaleCreateView.as_view(), name='new-sale'), 

    path("purchases/<billno>", views.PurchaseBillView.as_view(), name="purchase-bill"),
    path("sales/<billno>", views.SaleBillView.as_view(), name="sale-bill"),
]