# Generated by Django 2.0 on 2018-01-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0012_remove_incidententry_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidententry',
            name='affected_items',
            field=models.ManyToManyField(blank=True, to='catalogs.Item'),
        ),
        migrations.AlterField(
            model_name='incidententry',
            name='affected_services',
            field=models.ManyToManyField(blank=True, to='catalogs.Service'),
        ),
    ]
