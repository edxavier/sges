# Generated by Django 2.0 on 2018-01-18 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0006_auto_20180117_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidentsubcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='IncidentSubcategory',
        ),
    ]
