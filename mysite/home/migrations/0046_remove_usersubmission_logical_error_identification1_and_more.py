# Generated by Django 4.2.13 on 2024-09-28 11:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0045_remove_tafeedback_feedbacks_feedback_content6_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usersubmission",
            name="logical_error_identification1",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="logical_error_identification2",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="logical_error_identification3",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="logical_error_identification4",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="logical_error_identification5",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="logical_error_identification6",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="logical_error_identification7",
        ),
    ]