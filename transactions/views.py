from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View, 
    ListView,
)
from django.contrib import messages
from .models import Purchase, Supplier
from .forms import PurchaseForm
from inventory.models import Stock


class PurchaseView(ListView):
    model = Purchase
    template_name = "purchases.html"


class PurchaseCreateView(View):
    form_class = PurchaseForm
    template_name = 'new_purchase.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            stockid = request.POST.get("stock")
            quantity = request.POST.get("quantity")
            stock = get_object_or_404(Stock, id=stockid)
            stock.quantity = stock.quantity + int(quantity)
            stock.save()
            form.save()
            messages.success(request, f"Stock has been purchased")
            return redirect('purchases')
        return render(request, self.template_name, {'form': form})