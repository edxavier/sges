# Generated by Django 2.0 on 2018-02-11 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0015_auto_20180211_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskentry',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_entries', to='operations.Task'),
        ),
    ]