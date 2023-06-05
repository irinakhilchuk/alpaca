from django.db import models

class Needles(models.Model):
    needles_size_choices = [
        ('2,5mm', '2,5mm'),
        ('3,0mm', '3,0mm'),
        ('3,5mm', '3,5mm'),
        ('4,0mm', '4,0mm'),
        ('4,5mm', '4,5mm'),
        ('5,0mm', '5,0mm'),
        ('5,5mm', '5,5mm'),
        ('6,0mm', '6,0mm'),
        ('6,5mm', '6,5mm'),]
    size=models.CharField(max_length=5, choices=needles_size_choices, default='5,0')
    class Meta:
        verbose_name_plural = "needles"
    def __str__(self):
        return self.size
        
class Manufacturer(models.Model):
    manufacturer_choices = [
        ('SandnesGarn', 'SandnesGarn'),
        ('GarnStudio', 'GarnStudio'),
        ('PiuBellaYarns', 'PiuBellaYarns'),
        ]
    name=models.CharField(max_length=20, choices=manufacturer_choices)
    def __str__(self):
        return self.name

class Yarn(models.Model):
    manufacturer=models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=40)
    #colour=models.ManyToManyField(Colour)
    #colour=models.ManyToManyField(Colour.objects.filter(colour_manufacturer__exact=yarn_manufacturer))
    def __str__(self):
        return self.name

class Colour(models.Model):
    yarn=models.ForeignKey(Yarn, on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=10)
    image=models.ImageField(upload_to=None)
    def __str__(self):
        return self.name



class Sweater(models.Model):
    name=models.CharField(max_length=20)
    needles=models.ManyToManyField(Needles)
    yarn=models.ForeignKey(Yarn, on_delete=models.CASCADE, default=1)
    image=models.ImageField(upload_to=None)
    def __str__(self):
        return self.name
