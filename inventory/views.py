from django.shortcuts import render                                         # 'render' function used to render a html page
from django.views.generic import (
    TemplateView, 
    CreateView, 
    DeleteView
)                                                                           # various views for class based views
from .models import Stock                                                   # imports models
from .forms import StockForm                                                # imports forms
from django.contrib import messages                                         # imports messages fuctions


class HomeView(TemplateView):                                               # class to render home page
    template_name = "home.html"                                             # 'home.html' used as the template

class InventoryListView(TemplateView):                                      # class to render inventory page
    #TODO: create a list view to display stock items
    template_name = "inventory.html"                                        # 'inventory.html' used as the template

class StockCreateView(CreateView):                                          # createview class to render new stock page
    model = Stock                                                           # setting 'Stock' model as model
    form_class = StockForm                                                  # setting 'StockForm' form as form
    template_name = "new_stock.html"                                        # 'new_stock.html' used as the template
    #BUG: success url doesn't work
    success_url = 'inventory'                                               # redirects to 'inventory' page in the url after submitting the form

"""
def new_stock(request):                                                     # new stock page function
    
    stockform = NewStockForm(request.POST)                                  # stores the new stock form in 'stockform' variable
    
    if request.method == 'POST':                                            # if block is executed when the POST request is recieved. Used to verify that data is recieved to be stored
        
        if stockform.is_valid():                                            # if block is executed only when the form is valid (all mandatory fields are filled)
            
            stock = stockform.save(commit=False)                            # saves the 'stockform' in a variable
            #thread.created_user = request.user                             # set 'created_user' field to current user logged in
            #thread.forum = forum                                           # set 'forum' field to current forum
            stock.save()                                                    # saves the form in the database
                        
            return redirect('inventory')                                    # redirects to 'inventory' page
        
        else:
        
            stockform = NewStockForm(request.POST)                          # stores the new stock form in 'stockform' variable. Resets the form
            messages.warning(request, f"Please fill all the fields")        # shows message when form is invalid
    
    return render(request, 'new_stock.html')                                # request to render the 'new_stock.html'
"""