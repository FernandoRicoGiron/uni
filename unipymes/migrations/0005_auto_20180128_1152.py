# Generated by Django 2.0.1 on 2018-01-28 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unipymes', '0004_encuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='Empresas_idEmpresa',
        ),
        migrations.RemoveField(
            model_name='encuesta',
            name='Servicios_idServicios',
        ),
        migrations.RemoveField(
            model_name='encuesta',
            name='Usuarios_idUsuario',
        ),
        migrations.DeleteModel(
            name='Encuesta',
        ),
    ]
