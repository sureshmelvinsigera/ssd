# Generated by Django 3.2.7 on 2021-10-14 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20211007_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthReportFeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation', models.TextField(blank=True, null=True)),
                ('astronaut_health_report', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='authentication.astronauthealthreport')),
                ('scientist', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='authentication.scientist')),
            ],
        ),
    ]
