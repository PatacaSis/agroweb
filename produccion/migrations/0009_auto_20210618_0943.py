# Generated by Django 2.2 on 2021-06-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0008_auto_20210617_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='catanimal',
            name='det',
            field=models.CharField(default=1, max_length=100, verbose_name='Nombre'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catanimal',
            name='cat',
            field=models.CharField(max_length=10, verbose_name='Categoría'),
        ),
    ]