# Generated by Django 3.2.3 on 2021-09-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0005_auto_20210910_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudios_cv',
            name='descripcion',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='experiencias_cv',
            name='descripcion',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
