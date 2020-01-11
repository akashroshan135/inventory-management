from django import forms
from .models import Stock

class NewStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'category', 'description', 'quantity']