# Generated by Django 2.2 on 2021-06-29 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('economico', '0006_auto_20210624_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='Dni')),
                ('nacimiento', models.CharField(max_length=50, verbose_name='Fecha de nacimiento')),
                ('domicilio', models.CharField(max_length=100, verbose_name='Domicilio')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='GastoMO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de pago')),
                ('categoria', models.CharField(choices=[('1', 'Encargado'), ('2', 'Ayudante'), ('3', 'Colaborador')], max_length=1)),
                ('area', models.CharField(choices=[('1', 'Tambo'), ('2', 'Ganadería'), ('3', 'Estructura'), ('4', 'Tractorista'), ('5', 'General')], max_length=1, verbose_name='Area de trabajo')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Salario')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='economico.Empleado')),
            ],
            options={
                'verbose_name': 'Gasto de Mano de Obra',
                'verbose_name_plural': 'Gastos de Mano de Obra',
            },
        ),
    ]
