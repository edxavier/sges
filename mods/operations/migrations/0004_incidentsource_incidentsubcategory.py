# Generated by Django 2.0 on 2018-01-18 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_auto_20180116_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Origen de incidente',
                'verbose_name_plural': 'Origen de incidentes',
            },
        ),
        migrations.CreateModel(
            name='IncidentSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sub-categorias de incidente',
                'verbose_name_plural': 'Sub-categorias de incidentes',
            },
        ),
    ]