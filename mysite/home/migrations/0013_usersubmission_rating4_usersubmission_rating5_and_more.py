# Generated by Django 4.2.13 on 2024-06-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0012_usersubmission_rating3"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersubmission",
            name="rating4",
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="rating5",
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="rating6",
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="rating7",
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
