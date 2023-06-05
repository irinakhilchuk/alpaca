# Generated by Django 4.2.1 on 2023-06-04 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_yarn_sweater'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yarn',
            old_name='yarn_manufacturer',
            new_name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='colour',
            name='colour_manufacturer',
        ),
        migrations.RemoveField(
            model_name='yarn',
            name='colour',
        ),
        migrations.AddField(
            model_name='colour',
            name='yarn',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gallery.yarn'),
        ),
    ]