# Generated by Django 2.0.1 on 2018-01-31 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unipymes', '0009_remove_encuesta_empresas_idempresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerEncuestas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empresas_idEmpresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unipymes.Empresa')),
                ('Encuestas_idEncuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unipymes.Encuesta')),
            ],
        ),
    ]
