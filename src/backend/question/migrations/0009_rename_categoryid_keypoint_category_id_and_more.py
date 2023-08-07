# Generated by Django 4.1.4 on 2023-08-06 23:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question", "0008_rename_category_keypoint_categoryid_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="keypoint",
            old_name="categoryId",
            new_name="category_id",
        ),
        migrations.RemoveField(
            model_name="solution",
            name="keypoint",
        ),
        migrations.RemoveField(
            model_name="userkeypointscore",
            name="keypoint",
        ),
        migrations.AddField(
            model_name="ability",
            name="ability",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="solution",
            name="type",
            field=models.CharField(
                choices=[("CO", "Coding"), ("CH", "Choice")],
                help_text="required solution type",
                max_length=2,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="type",
            field=models.CharField(
                default="default_type", help_text="type of the question", max_length=20
            ),
        ),
    ]
