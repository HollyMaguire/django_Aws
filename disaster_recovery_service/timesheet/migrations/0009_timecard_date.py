# Generated by Django 3.2.7 on 2021-09-10 22:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0008_auto_20210910_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='timecard',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
