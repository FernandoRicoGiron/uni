# Generated by Django 2.0.1 on 2018-01-31 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unipymes', '0010_verencuestas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verencuestas',
            name='Empresas_idEmpresa',
        ),
        migrations.RemoveField(
            model_name='verencuestas',
            name='Encuestas_idEncuesta',
        ),
        migrations.AddField(
            model_name='encuesta',
            name='Empresas_idEmpresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='unipymes.Empresa'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='VerEncuestas',
        ),
    ]
