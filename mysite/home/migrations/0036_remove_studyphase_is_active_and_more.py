# Generated by Django 4.2.13 on 2024-09-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0035_studyphase"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studyphase",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="studyphase",
            name="phase_name",
        ),
        migrations.AddField(
            model_name="studyphase",
            name="current_phase",
            field=models.CharField(default="phase1", max_length=20),
        ),
    ]