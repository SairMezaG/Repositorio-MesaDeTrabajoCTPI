# Generated by Django 5.0.6 on 2024-05-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMesaServicio', '0002_tipoprocedimiento_solicitud_caso_solucioncaso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoprocedimiento',
            name='tipDescripcion',
            field=models.TextField(db_comment='Aquí se hace una descripción del tipo de procedimiento', max_length=1000, null=True),
        ),
    ]
