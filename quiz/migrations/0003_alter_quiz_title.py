# Generated by Django 3.2.23 on 2024-03-12 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_choice_id_alter_progress_id_alter_question_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]