# Generated by Django 2.2.4 on 2020-06-14 10:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmiapp', '0002_auto_20200613_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmi',
            name='height',
            field=models.IntegerField(default='1', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5000)]),
        ),
    ]
