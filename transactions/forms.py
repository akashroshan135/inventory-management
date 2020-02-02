from django import forms
from django.forms import formset_factory
from .models import (
    PurchaseBill, 
    PurchaseItem, 
    Supplier, 
    SaleBill, 
    SaleItem
)



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


class SupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = Supplier
        fields = ['name', 'phone', 'email']



class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'required': 'true'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = SaleBill
        fields = ['name', 'phone', 'email']


class SaleItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setquantity', 'required': 'true'})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control putprice', 'required': 'true', 'disabled': 'true'})
    class Meta:
        model = SaleItem
        fields = ['stock', 'quantity', 'price']

SaleItemFormset = formset_factory(SaleItemForm, extra=1)