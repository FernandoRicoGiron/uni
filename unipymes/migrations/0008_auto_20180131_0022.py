# Generated by Django 2.0.1 on 2018-01-31 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unipymes', '0007_auto_20180130_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encuesta',
            old_name='Empresas_idEmpresas',
            new_name='Empresas_idEmpresa',
        ),
    ]
