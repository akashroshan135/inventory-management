import django_filters
from .models import PurchaseBill, SaleBill    

class SaleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = SaleBill
        fields = ['name']