from django import forms
from .models import PurchaseBill, PurchaseStock


class SelectSupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = PurchaseBill
        fields = ['supplier']


class PurchaseBillForm(forms.ModelForm):
    class Meta:
        model = PurchaseBill
        fields = ['billno', 'supplier']

class PurchaseStockForm(forms.ModelForm):
    class Meta:
        model = PurchaseStock
        fields = ['stock', 'quantity', 'price']