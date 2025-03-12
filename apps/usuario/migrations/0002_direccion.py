# Generated by Django 5.1.6 on 2025-02-18 03:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=200)),
                ('numero_exterior', models.CharField(blank=True, max_length=20, null=True)),
                ('numero_interior', models.CharField(blank=True, max_length=20, null=True)),
                ('codigo_postal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='direccion.codigopostal')),
                ('colonia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.colonia')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.estado')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.municipio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
