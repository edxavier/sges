# Generated by Django 2.0 on 2018-01-02 20:48

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
                ('cod_emp', models.PositiveIntegerField()),
                ('active', models.BooleanField(default=True)),
                ('valid_weeks', models.PositiveIntegerField(default=4)),
                ('rol_end', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Empleados',
                'verbose_name': 'Empleado',
            },
        ),
        migrations.CreateModel(
            name='EmployeRol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Employe')),
            ],
            options={
                'verbose_name_plural': 'Horario Empleados',
                'verbose_name': 'Entrada',
            },
        ),
        migrations.CreateModel(
            name='Matrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('tasks', models.CharField(blank=True, max_length=100, null=True)),
                ('total_hours', models.IntegerField(default=48)),
                ('worked_hours', models.IntegerField(default=48)),
                ('extras', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Matriz',
                'verbose_name': 'Rol Matriz',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(default='', max_length=20)),
                ('workin_hours', models.IntegerField(default=8)),
            ],
            options={
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.AddField(
            model_name='matrix',
            name='friday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friday', to='schedule.Rol', verbose_name='Viernes'),
        ),
        migrations.AddField(
            model_name='matrix',
            name='monday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monday', to='schedule.Rol', verbose_name='Lunes'),
        ),
        migrations.AddField(
            model_name='matrix',
            name='saturday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saturday', to='schedule.Rol', verbose_name='Sabado'),
        ),
        migrations.AddField(
            model_name='matrix',
            name='sunday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sunday', to='schedule.Rol', verbose_name='Domingo'),
        ),
        migrations.AddField(
            model_name='matrix',
            name='thursday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thursday', to='schedule.Rol', verbose_name='Jueves'),
        ),
        migrations.AddField(
            model_name='matrix',
            name='tuesday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuesday', to='schedule.Rol', verbose_name='Martes'),
        ),
        migrations.AddField(
            model_name='matrix',
            name='wednesday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wednesday', to='schedule.Rol', verbose_name='Miercoles'),
        ),
        migrations.AddField(
            model_name='employerol',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Matrix'),
        ),
        migrations.AddField(
            model_name='employe',
            name='last_rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Matrix'),
        ),
    ]