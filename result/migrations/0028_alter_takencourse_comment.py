# Generated by Django 3.2.23 on 2024-03-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0027_alter_takencourse_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[(' 25/03/24', ' 25/03/24'), ('* 25/03/24', '* 25/03/24')], max_length=200),
        ),
    ]
