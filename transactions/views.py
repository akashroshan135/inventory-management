from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View, 
    ListView,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import (
    PurchaseBill, 
    Supplier, 
    PurchaseItem, 
    SaleBill,  
    SaleItem
)
from .forms import (
    SelectSupplierForm, 
    PurchaseItemFormset, 
    SupplierForm, 
    SaleForm,
    SaleItemFormset
)
from inventory.models import Stock


# shows the list of bills of all purchases 
class PurchaseView(View):
    model = PurchaseBill
    template_name = "purchases/purchases_list.html"

    def get(self, request, *args, **kwargs):
        bills = PurchaseBill.objects.all()
        return render(request, self.template_name, {'bills': bills})

# used to select the supplier
class SelectSupplierView(View):
    form_class = SelectSupplierForm
    template_name = 'purchases/select_supplier.html'

    def get(self, request, *args, **kwargs):                                    # loads the form page
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):                                   # gets selected supplier and redirects to 'PurchaseCreateView' class
        form = self.form_class(request.POST)
        if form.is_valid():
            supplierid = request.POST.get("supplier")
            supplier = get_object_or_404(Supplier, id=supplierid)
            return redirect('new-purchase', supplier.pk)
        return render(request, self.template_name, {'form': form})

# used to generate a bill object and save items 
class PurchaseCreateView(View):                                                 
    template_name = 'purchases/new_purchase.html'

    def get(self, request, pk):
        formset = PurchaseItemFormset(request.GET or None)                      # renders an empty formset
        supplierobj = get_object_or_404(Supplier, pk=pk)                        # gets the supplier object
        stocks = Stock.objects.all()
        context = {
            'formset'   : formset,
            'supplier'  : supplierobj,
            'stocks'    : stocks
        }                                                                       # sends the supplier and formset as context
        return render(request, self.template_name, context)

    def post(self, request, pk):
        formset = PurchaseItemFormset(request.POST)                             # recieves a post method for the formset
        supplierobj = get_object_or_404(Supplier, pk=pk)                        # gets the supplier object
        if formset.is_valid():
            billobj = PurchaseBill(supplier=supplierobj)                        # a new object of class 'PurchaseBill' is created with supplier field set to 'supplierobj'
            billobj.save()                                                      # saves object into the db
            for form in formset:                                                # for loop to save each individual form as its own object
                billitem = form.save(commit=False)
                billitem.billno = billobj                                       # links the bill object to the items
                item = get_object_or_404(Stock, name=billitem.stock.name)       # gets the item
                item.quantity += billitem.quantity                              # updates quantity
                item.save()
                billitem.save()
            messages.success(request, "Purchased items have been registered successfully")
            return redirect('purchases-list')
        formset = PurchaseItemFormset(request.GET or None)
        context = {
            'formset'   : formset,
            'supplier'  : supplierobj
        }
        return render(request, self.template_name, context)


# shows a lists of all suppliers
class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers/suppliers_list.html"

# used to add a new supplier
class SupplierCreateView(SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    success_url = '/transactions/suppliers'
    success_message = "Supplier has been created successfully"
    template_name = "suppliers/edit_supplier.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Supplier'
        context["savebtn"] = 'Add Supplier'
        return context     

# used to update a suppliers info
class SupplierUpdateView(SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    success_url = '/transactions/suppliers'
    success_message = "Supplier details has been updated successfully"
    template_name = "suppliers/edit_supplier.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Supplier'
        context["savebtn"] = 'Save Changes'
        context["delbtn"] = 'Delete Supplier'
        return context

# used to view a supplier's profile TODO: add charts
class SupplierView(View):
    def get(self, request, name):
        supplierobj = get_object_or_404(Supplier, name=name)
        bills = PurchaseBill.objects.filter(supplier=supplierobj)
        context = {
            'supplier'  : supplierobj,
            'bills'     : bills
        }
        return render(request, 'suppliers/supplier.html', context)


# shows a list of all sales bills
class SaleView(View):
    model = SaleBill
    template_name = "sales/sales_list.html"

    def get(self, request, *args, **kwargs):
        bills = SaleBill.objects.all()
        return render(request, self.template_name, {'bills': bills})

# used to generate a bill object and save items
class SaleCreateView(View):                                                      
    template_name = 'sales/new_sale.html'

    def get(self, request):
        form = SaleForm(request.GET or None)
        formset = SaleItemFormset(request.GET or None)                          # renders an empty formset
        stocks = Stock.objects.all()
        context = {
            'form'      : form,
            'formset'   : formset,
            'stocks'     : stocks
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SaleForm(request.POST)
        formset = SaleItemFormset(request.POST)                             # recieves a post method for the formset
        if form.is_valid() and formset.is_valid():
            billobj = form.save(commit=False)
            billobj.save()     
            for form in formset:                                                # for loop to save each individual form as its own object
                billitem = form.save(commit=False)
                billitem.billno = billobj                                       # links the bill object to the items
                item = get_object_or_404(Stock, name=billitem.stock.name)       # gets the item
                item.quantity -= billitem.quantity                              # updates quantity
                item.save()
                billitem.save()
            messages.success(request, "Sold items have been registered successfully")
            return redirect('sales-list')
        form = SaleForm(request.GET or None)
        formset = SaleItemFormset(request.GET or None)
        context = {
            'form'      : form,
            'formset'   : formset,
        }
        return render(request, self.template_name, context)

#TODO: create bill view for both purchases and sales