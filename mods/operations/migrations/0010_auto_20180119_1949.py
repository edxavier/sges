# Generated by Django 2.0 on 2018-01-20 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0009_auto_20180119_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidententry',
            name='incident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incident_entries', to='operations.Incident'),
        ),
    ]
