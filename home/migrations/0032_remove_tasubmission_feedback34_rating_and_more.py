# Generated by Django 4.2.13 on 2024-09-12 18:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "home",
            "0031_rename_feedback1_rating_tasubmission_feedback11_rating_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tasubmission",
            name="feedback34_rating",
        ),
        migrations.RemoveField(
            model_name="tasubmission",
            name="feedback35_rating",
        ),
    ]
