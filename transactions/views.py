from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View, 
    ListView,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import PurchaseBill, Supplier, PurchaseItem
from .forms import SelectSupplierForm, PurchaseItemFormset, SupplierForm
from inventory.models import Stock



class PurchaseView(View):
    model = PurchaseBill
    template_name = "purchases/purchases_list.html"

    def get(self, request, *args, **kwargs):
        bills = PurchaseBill.objects.all()
        return render(request, self.template_name, {'bills': bills})


class SelectSupplierView(View):                                                 # CBV used to select the suppiler
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


class PurchaseCreateView(View):                                                 # used to generate a bill object and save items 
    template_name = 'purchases/new_purchase.html'

    def get(self, request, pk):
        formset = PurchaseItemFormset(request.GET or None)                      # renders an empty formset
        supplierobj = get_object_or_404(Supplier, pk=pk)                        # gets the supplier object
        context = {
            'formset'   : formset,
            'supplier'  : supplierobj
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
            return redirect('purchases')
        context = {
            'formset'   : formset,
            'supplier'  : supplierobj
        }
        return render(request, self.template_name, context)



class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers/suppliers_list.html"


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