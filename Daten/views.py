from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Geburtstage

def index(request):
    
    return render(request, 'Daten/liste.html', {})

# Create your views here.
