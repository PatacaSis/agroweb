# Generated by Django 2.2 on 2021-07-01 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0018_auto_20210625_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='ms',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True, verbose_name='Materia Seca'),
        ),
        migrations.AddField(
            model_name='alimento',
            name='pt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True, verbose_name='Porcentaje proteico'),
        ),
    ]