# Generated by Django 4.2.13 on 2024-06-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0015_remove_usersubmission_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usersubmission",
            name="understandability",
            field=models.CharField(max_length=50),
        ),
    ]
