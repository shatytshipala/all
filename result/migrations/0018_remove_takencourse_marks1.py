# Generated by Django 3.2.23 on 2024-03-09 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0017_auto_20240309_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takencourse',
            name='Marks1',
        ),
    ]