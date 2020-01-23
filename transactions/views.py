from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View, 
    ListView,
)
from django.contrib import messages
from inventory.models import Stock
from .models import PurchaseBill, Supplier
from .forms import SelectSupplierForm, PurchaseStockForm


class PurchaseView(ListView):
    model = PurchaseBill
    template_name = "purchases.html"


class SelectSupplierView(View):
    form_class = SelectSupplierForm
    template_name = 'select_supplier.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            supplierid = request.POST.get("supplier")
            supplier = get_object_or_404(Supplier, id=supplierid)
            return redirect('new-purchase', supplier.pk)
        return render(request, self.template_name, {'form': form})


class PurchaseCreateView(View):
    form_class = PurchaseStockForm
    template_name = 'new_purchase.html'

    def get(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        context = {
            'supplier'  : supplier, 
            'stockform' : self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            supplierobj = get_object_or_404(Supplier, pk=pk)
            billobj = PurchaseBill(supplier=supplierobj)
            billobj.save()

            obj = form.save(commit=False)
            obj.billno = billobj
            obj.save()
            return redirect('purchases')
        return render(request, self.template_name, {'form': form})