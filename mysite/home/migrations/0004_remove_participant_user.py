# Generated by Django 4.2.13 on 2024-06-13 04:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_product_remove_participant_organisation_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="participant",
            name="user",
        ),
    ]