from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from Daten.models import Geburtstage


def index(request):
    geb = Geburtstage.objects.order_by('geburtstag')

    return render(request, 'Startseite/liste1.html', {
        'geb': geb,
    })
