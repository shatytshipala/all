# Generated by Django 3.2.23 on 2024-03-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_newsandevents_id_alter_semester_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.CharField(blank=True, choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('FOURTH', 'FOURTH')], max_length=10),
        ),
    ]
