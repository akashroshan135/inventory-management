from django import forms
from django.forms import formset_factory
from .models import PurchaseBill, PurchaseItem


class SelectSupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = PurchaseBill
        fields = ['supplier']


class PurchaseItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
    class Meta:
        model = PurchaseItem
        fields = ['stock', 'quantity', 'price']

PurchaseItemFormset = formset_factory(PurchaseItemForm, extra=1)