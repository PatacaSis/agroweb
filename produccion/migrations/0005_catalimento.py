# Generated by Django 2.2 on 2021-06-17 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0004_catanimal'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatAlimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100, verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Categoría de alimento',
                'verbose_name_plural': 'Categoría alimentos',
                'ordering': ('cat',),
            },
        ),
    ]
