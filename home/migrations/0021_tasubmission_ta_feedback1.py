# Generated by Django 4.2.13 on 2024-07-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0020_tasubmission_ta_logical_error_identification2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tasubmission",
            name="ta_feedback1",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]