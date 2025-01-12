# Generated by Django 4.2.13 on 2024-09-25 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0043_rename_content11_feedback_content1_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feedback",
            name="content6",
        ),
        migrations.RemoveField(
            model_name="feedback",
            name="content7",
        ),
        migrations.AddField(
            model_name="tafeedback",
            name="feedbacks",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.feedback",
            ),
            preserve_default=False,
        ),
    ]