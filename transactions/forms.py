from django import forms
from .models import PurchaseBill, PurchaseStock


class SelectSupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = PurchaseBill
        fields = ['supplier']


class PurchaseStockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = PurchaseStock
        fields = ['stock', 'quantity', 'price']