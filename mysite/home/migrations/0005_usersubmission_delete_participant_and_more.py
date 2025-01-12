# Generated by Django 4.2.13 on 2024-06-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_remove_participant_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserSubmission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=200)),
                ("rating", models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name="Participant",
        ),
        migrations.RemoveField(
            model_name="rating",
            name="product",
        ),
        migrations.RemoveField(
            model_name="rating",
            name="user",
        ),
        migrations.DeleteModel(
            name="Product",
        ),
        migrations.DeleteModel(
            name="Rating",
        ),
    ]