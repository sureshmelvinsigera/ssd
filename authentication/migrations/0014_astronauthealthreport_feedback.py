# Generated by Django 3.2.7 on 2021-10-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_delete_healthreportfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='astronauthealthreport',
            name='feedback',
            field=models.TextField(blank=True, default='No feedback as of yet', null=True),
        ),
    ]