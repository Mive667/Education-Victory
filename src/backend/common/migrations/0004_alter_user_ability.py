# Generated by Django 4.1.4 on 2023-08-27 03:18

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_user_solved_prblem_alter_user_target_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ability',
            field=models.JSONField(default=common.models.get_default_ability),
        ),
    ]
