# Generated by Django 3.2.7 on 2021-09-30 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20210930_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='astronaut',
            name='blood_pressure',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='astronaut',
            name='blood_type',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='astronaut',
            name='heart_rate',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='astronaut',
            name='muscle_mass',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='astronaut',
            name='weight',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scientist',
            name='specialty',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]