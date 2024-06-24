# Generated by Django 4.2.13 on 2024-06-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMesaServicio', '0005_alter_caso_cascodigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fechaHoraActualizacion',
            field=models.DateField(auto_now=True, db_comment='Fecha y hora última actualización'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fechaHoraCreacion',
            field=models.DateField(auto_now_add=True, db_comment='Fecha y hora del registro'),
        ),
    ]
