# Generated by Django 2.0.6 on 2018-06-30 22:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('unipymes', '0007_auto_20180630_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje_solicitud',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
