from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    """ a view to return the index page """
    return render(request, 'home/index.html')