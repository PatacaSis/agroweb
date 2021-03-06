# Generated by Django 2.2 on 2021-06-17 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
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
        migrations.CreateModel(
            name='CatAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100, verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Categoría animal',
                'verbose_name_plural': 'Categoría animales',
                'ordering': ('cat',),
            },
        ),
        migrations.AlterField(
            model_name='prodleche',
            name='temp',
            field=models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Temperatura entregada'),
        ),
        migrations.CreateModel(
            name='ExistenciaAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('grupo', models.CharField(choices=[(1, 'Rodeo/Leche'), (2, 'Carne')], max_length=30)),
                ('cantidad', models.IntegerField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produccion.CatAnimal')),
            ],
            options={
                'verbose_name': 'Existencia animal',
                'verbose_name_plural': 'Existencias animales',
                'ordering': ('cat',),
            },
        ),
    ]
