from django.shortcuts import render

def home(request):
    return render(request, 'home.html')                 # request to render the home.html