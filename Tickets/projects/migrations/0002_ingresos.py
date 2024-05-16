# Generated by Django 5.0.4 on 2024-05-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingresos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anno', models.CharField(max_length=100)),
                ('mes', models.CharField(max_length=100)),
                ('colombia_telecomunicaciones', models.CharField(max_length=100)),
                ('colombia_movil', models.CharField(max_length=100)),
                ('comunicacion_celular_comcel', models.CharField(max_length=100)),
                ('empresa_de_telecomunicaciones_de_bogota', models.CharField(max_length=100)),
                ('une_epm', models.CharField(max_length=100)),
                ('avantel', models.CharField(max_length=100)),
                ('almacenes_exito', models.CharField(max_length=100)),
                ('virgin_mobile', models.CharField(max_length=100)),
                ('partners_telecom', models.CharField(max_length=100)),
                ('setroc_mobile', models.CharField(max_length=100)),
                ('uff_movil', models.CharField(max_length=100)),
                ('cellvoz_colombia', models.CharField(max_length=100)),
                ('logistica_flash', models.CharField(max_length=100)),
                ('lov_telecomunicaciones', models.CharField(max_length=100)),
                ('suma_movil', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['anno'],
            },
        ),
    ]
