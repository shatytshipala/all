# pylint: disable-all
# Generated by Django 2.2.3 on 2020-07-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='session',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
