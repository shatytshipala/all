# Generated by Django 3.2.23 on 2024-03-10 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0020_auto_20240310_0927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='takencourse',
            old_name='attendan',
            new_name='marks_1',
        ),
    ]
