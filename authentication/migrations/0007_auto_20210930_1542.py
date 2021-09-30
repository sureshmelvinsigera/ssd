# Generated by Django 3.2.7 on 2021-09-30 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('authentication', '0006_astronaut_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astronaut',
            name='astronaut_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='scientist_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
        ),
        migrations.DeleteModel(
            name='SystemUser',
        ),
    ]
