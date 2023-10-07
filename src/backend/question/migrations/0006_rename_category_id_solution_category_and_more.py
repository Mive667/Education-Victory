# Generated by Django 4.1.4 on 2023-09-01 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_alter_choicequestion_choice_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='problem_id',
            new_name='problem',
        ),
        migrations.RenameField(
            model_name='testcase',
            old_name='coding_question_id',
            new_name='coding_question',
        ),
        migrations.RemoveField(
            model_name='choicequestion',
            name='solution_id',
        ),
        migrations.RemoveField(
            model_name='codingquestion',
            name='solution_id',
        ),
    ]