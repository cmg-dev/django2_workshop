from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Geburtstage

def index(request):
    geb = Geburtstage.objects.all()
    
    return render(request, 'Daten/liste.html', {
        'geb' : geb,
    })

# Create your views here.
