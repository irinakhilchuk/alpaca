from django.shortcuts import render
from gallery.models import Sweater

def layout(request):
    sweaters = Sweater.objects.all
    return render(request, 'gallery.html', context={'sweaters':sweaters})
# Create your views here.
