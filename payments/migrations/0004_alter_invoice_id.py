# pylint: disable-all
# Generated by Django 4.1.6 on 2023-02-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_delete_testclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
