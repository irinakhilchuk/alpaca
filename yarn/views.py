from django.shortcuts import render
from gallery.models import Sweater

def yarns(request):
    sweaters = Sweater.objects.all
    return render(request, 'yarncolours.html', context={'sweaters':sweaters})

