# Generated by Django 4.2.13 on 2024-10-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0048_remove_feedback_content6_remove_feedback_content7"),
    ]

    operations = [
        migrations.AddField(
            model_name="tafeedback",
            name="rollno",
            field=models.CharField(default="bt22cse121", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tasubmission",
            name="rollno",
            field=models.CharField(default="bt22cse21", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="rollno",
            field=models.CharField(default="bt22cse212", max_length=20),
            preserve_default=False,
        ),
    ]
