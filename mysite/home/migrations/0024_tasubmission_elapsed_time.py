# Generated by Django 4.2.13 on 2024-07-31 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0023_tasubmission_designation_tasubmission_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tasubmission",
            name="elapsed_time",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
