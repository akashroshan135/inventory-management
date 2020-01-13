from django.shortcuts import render                                         # 'render' function used to render a html page
from .forms import NewStockForm
from django.contrib import messages

def home(request):                                                          # home page function
    return render(request, 'home.html')                                     # request to render the 'home.html'

def inventory(request):                                                     # inventory page function
    return render(request, 'inventory.html', context=None)                  # request to render the 'inventory.html'

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