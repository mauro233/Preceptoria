# Generated by Django 2.2.5 on 2019-11-13 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('profesor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('dia', models.CharField(help_text='Escriba el dia en el que dicte la materia', max_length=50)),
                ('materia', models.ForeignKey(help_text='Seleccion la materia', on_delete=django.db.models.deletion.CASCADE, related_name='materiaId', to='horario.Materia')),
            ],
        ),
    ]