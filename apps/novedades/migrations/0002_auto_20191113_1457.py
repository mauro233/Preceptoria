# Generated by Django 2.2.5 on 2019-11-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='fecha',
            field=models.DateField(auto_now_add=True, help_text='Fecha de publicacion'),
        ),
    ]
