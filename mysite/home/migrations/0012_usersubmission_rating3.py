# Generated by Django 4.2.13 on 2024-06-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_usersubmission_rating2"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersubmission",
            name="rating3",
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
