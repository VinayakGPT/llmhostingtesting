# Generated by Django 4.2.13 on 2024-09-24 18:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0040_alter_tafeedback_ta_feedback1_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Feedbacks",
            new_name="Feedback",
        ),
    ]