# Generated by Django 4.2.13 on 2024-06-17 13:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_usersubmission_problem2_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usersubmission",
            name="problem2_rating",
        ),
    ]
