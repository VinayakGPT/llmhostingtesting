# Generated by Django 4.2.13 on 2024-09-11 06:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0028_tafeedback_remove_tasubmission_ta_feedback1_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tafeedback",
            name="designation",
        ),
        migrations.RemoveField(
            model_name="tasubmission",
            name="designation",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="designation",
        ),
    ]
