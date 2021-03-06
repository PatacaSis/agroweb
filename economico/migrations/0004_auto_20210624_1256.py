# Generated by Django 2.2 on 2021-06-24 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('economico', '0003_auto_20210624_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Umedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Rubro')),
            ],
            options={
                'verbose_name': 'U.medida',
                'verbose_name_plural': 'U.medidas',
                'ordering': ['nombre'],
            },
        ),
        migrations.AlterField(
            model_name='gasto',
            name='unidades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='economico.Umedida'),
        ),
    ]
