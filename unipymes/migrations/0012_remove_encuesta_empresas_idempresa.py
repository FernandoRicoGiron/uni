# Generated by Django 2.0.1 on 2018-02-04 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unipymes', '0011_auto_20180131_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='Empresas_idEmpresa',
        ),
    ]
