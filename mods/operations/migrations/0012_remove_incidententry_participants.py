# Generated by Django 2.0 on 2018-01-20 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0011_auto_20180119_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidententry',
            name='participants',
        ),
    ]