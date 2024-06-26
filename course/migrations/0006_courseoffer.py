# pylint: disable-all
# Generated by Django 4.1.6 on 2023-05-14 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0014_alter_user_managers"),
        ("course", "0005_alter_course_id_alter_courseallocation_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseOffer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dep_head",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.departmenthead",
                    ),
                ),
            ],
        ),
    ]
