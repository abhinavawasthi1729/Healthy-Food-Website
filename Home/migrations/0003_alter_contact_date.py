# Generated by Django 3.2.5 on 2021-07-22 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20210723_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 23, 2, 3, 42, 786832)),
        ),
    ]