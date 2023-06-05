from django.contrib import admin
from .models import Needles, Manufacturer, Colour, Yarn, Sweater

admin.site.register(Needles)
admin.site.register(Manufacturer)
admin.site.register(Colour)
admin.site.register(Yarn)
admin.site.register(Sweater)
# Register your models here.
