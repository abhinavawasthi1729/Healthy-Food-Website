# Generated by Django 3.2.5 on 2021-07-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default='no comments'),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='abc@gmail.com', max_length=122),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='abc', max_length=122),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='123', max_length=12),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default='1/1/2000'),
        ),
    ]
