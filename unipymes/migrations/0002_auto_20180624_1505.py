# Generated by Django 2.0.6 on 2018-06-24 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('unipymes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaNacimiento', models.DateField(blank=True, null=True)),
                ('Telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('EstadoCivil', models.CharField(blank=True, max_length=50, null=True)),
                ('Sexo', models.CharField(blank=True, max_length=50, null=True)),
                ('Escolaridad', models.CharField(blank=True, max_length=50, null=True)),
                ('Estado', models.CharField(blank=True, max_length=50, null=True)),
                ('Municipio', models.CharField(blank=True, max_length=50, null=True)),
                ('Domicilio', models.CharField(blank=True, max_length=50, null=True)),
                ('NumExterior', models.CharField(blank=True, max_length=50, null=True)),
                ('NumInterior', models.CharField(blank=True, max_length=50, null=True)),
                ('CodigoPostal', models.CharField(blank=True, max_length=50, null=True)),
                ('Correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('Usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Empresa',
        ),
        migrations.RenameField(
            model_name='encuesta',
            old_name='Empresas_idEmpresa',
            new_name='Empresa',
        ),
        migrations.RenameField(
            model_name='servicio',
            old_name='Carrera',
            new_name='Area',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='Convocatoria',
        ),
        migrations.AddField(
            model_name='empresa',
            name='Usuario',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='Imagen',
            field=models.ImageField(default='', upload_to='Servicios'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Calle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='CodigoPostal',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='NumExterior',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='NumInterior',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='RFC',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='SitioWeb',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Telefono',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='Cinco',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='Cuatro',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='Dos',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='Tres',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='Uno',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='espera',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='Asunto',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='Estado',
            field=models.CharField(choices=[('Sin Responder', 'Sin Responder'), ('Respondido', 'Respondido')], default='Sin Responder', max_length=50),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='Precio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='solicitude',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
