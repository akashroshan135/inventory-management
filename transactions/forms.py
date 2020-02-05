from django import forms
from django.forms import formset_factory
from .models import (
    PurchaseBill, 
    PurchaseItem, 
    Supplier, 
    SaleBill, 
    SaleItem
)


# form used to select a supplier
class SelectSupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = PurchaseBill
        fields = ['supplier']

# form used to render a single stock item form
class PurchaseItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setquantity', 'required': 'true'})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control putprice', 'required': 'true', 'readonly': 'true'})
    class Meta:
        model = PurchaseItem
        fields = ['stock', 'quantity', 'price']

# formset used to render multiple 'PurchaseItemForm'
PurchaseItemFormset = formset_factory(PurchaseItemForm, extra=1)


# form used for supplier
class SupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = Supplier
        fields = ['name', 'phone', 'email']


# form used to get customer details
class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'required': 'true'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'required': 'true'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = SaleBill
        fields = ['name', 'phone', 'email']

# form used to render a single stock item form
class SaleItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setquantity', 'required': 'true'})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control putprice', 'required': 'true', 'readonly': 'true'})
    class Meta:
        model = SaleItem
        fields = ['stock', 'quantity', 'price']

# formset used to render multiple 'SaleItemForm'
SaleItemFormset = formset_factory(SaleItemForm, extra=1)