# Generated by Django 3.2.7 on 2021-09-30 15:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210930_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='astronaut',
            name='age',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(
                100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
