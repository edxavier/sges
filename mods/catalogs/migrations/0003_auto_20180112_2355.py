# Generated by Django 2.0 on 2018-01-13 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogs', '0002_auto_20180111_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemhistory',
            name='modificated_at',
        ),
        migrations.AddField(
            model_name='itemhistory',
            name='created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
