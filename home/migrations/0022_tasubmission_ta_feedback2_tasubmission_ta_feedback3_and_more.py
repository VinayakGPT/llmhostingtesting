# Generated by Django 4.2.13 on 2024-07-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0021_tasubmission_ta_feedback1"),
    ]

    operations = [
        migrations.AddField(
            model_name="tasubmission",
            name="ta_feedback2",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tasubmission",
            name="ta_feedback3",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tasubmission",
            name="ta_feedback4",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tasubmission",
            name="ta_feedback5",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tasubmission",
            name="ta_feedback6",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tasubmission",
            name="ta_feedback7",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
