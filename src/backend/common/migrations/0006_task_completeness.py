# Generated by Django 4.1.4 on 2023-08-30 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_task_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completeness',
            field=models.CharField(default='Start', max_length=100),
        ),
    ]