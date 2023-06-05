# Generated by Django 4.2.1 on 2023-06-04 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('SandnesGarn', 'SandnesGarn'), ('GarnStudio', 'GarnStudio'), ('PiuBellaYarns', 'PiuBellaYarns')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Needles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('2,5mm', '2,5mm'), ('3,0mm', '3,0mm'), ('3,5mm', '3,5mm'), ('4,0mm', '4,0mm'), ('4,5mm', '4,5mm'), ('5,0mm', '5,0mm'), ('5,5mm', '5,5mm'), ('6,0mm', '6,0mm'), ('6,5mm', '6,5mm')], default='5,0', max_length=5)),
            ],
            options={
                'verbose_name_plural': 'needles',
            },
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to=None)),
                ('colour_manufacturer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gallery.manufacturer')),
            ],
        ),
    ]