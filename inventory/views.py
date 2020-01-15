from django.shortcuts import render                                         # 'render' function used to render a html page
from django.views.generic import (
    TemplateView, 
    ListView,
    CreateView, 
    UpdateView,
    DeleteView
)                                                                           # various views for class based views
from .models import Stock                                                   # imports models
from .forms import StockForm                                                # imports forms
from django.contrib.messages.views import SuccessMessageMixin               # mixin used to display success message



class HomeView(TemplateView):                                               # class to render home page
    template_name = "home.html"                                             # 'home.html' used as the template


class InventoryListView(ListView):                                          # class to render inventory page
    model = Stock                                                           # setting 'Stock' model as model
    context_object_name = 'stock_items'                                     # 'Stock' model set as 'stock_items' context
    template_name = "inventory.html"                                        # 'inventory.html' used as the template


class StockCreateView(SuccessMessageMixin, CreateView):                     # createview class to render new stock page, mixin used to display message
    model = Stock                                                           # setting 'Stock' model as model
    form_class = StockForm                                                  # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                       # 'edit_stock.html' used as the template
    success_url = '/inventory'                                              # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been created successfully"                 # displays message when form is submitted

    def get_context_data(self, **kwargs):                                   # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Stock'
        context["savebtn"] = 'Add to Inventory'
        return context       


class StockUpdateView(SuccessMessageMixin, UpdateView):                     # update view class to render new stock page, mixin used to display message
    model = Stock                                                           # setting 'Stock' model as model
    form_class = StockForm                                                  # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                       # 'edit_stock.html' used as the template
    success_url = '/inventory'                                              # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been updated successfully"                 # displays message when form is submitted

    def get_context_data(self, **kwargs):                                   # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Stock'
        context["savebtn"] = 'Update Stock'
        context["delbtn"] = 'Delete Stock'
        return context