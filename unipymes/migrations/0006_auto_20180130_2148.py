# Generated by Django 2.0.1 on 2018-01-31 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unipymes', '0005_auto_20180130_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuestasec',
            name='Empresas_idEmpresa',
        ),
        migrations.RemoveField(
            model_name='encuestasec',
            name='Encuestas_idEncuesta',
        ),
        migrations.AddField(
            model_name='encuesta',
            name='Empresas_idEmpresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='unipymes.Empresa'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Encuestasec',
        ),
    ]