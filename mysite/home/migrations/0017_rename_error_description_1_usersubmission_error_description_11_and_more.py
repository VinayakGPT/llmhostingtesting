# Generated by Django 4.2.13 on 2024-06-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0016_alter_usersubmission_understandability"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usersubmission",
            old_name="error_description_1",
            new_name="error_description_11",
        ),
        migrations.RenameField(
            model_name="usersubmission",
            old_name="error_description_2",
            new_name="error_description_12",
        ),
        migrations.RenameField(
            model_name="usersubmission",
            old_name="feedback_reveal",
            new_name="error_description_21",
        ),
        migrations.RenameField(
            model_name="usersubmission",
            old_name="logical_error_identification",
            new_name="error_description_22",
        ),
        migrations.RenameField(
            model_name="usersubmission",
            old_name="understandability",
            new_name="understandability1",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="rating2",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="rating3",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="rating4",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="rating5",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="rating6",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="rating7",
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_31",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_32",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_41",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_42",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_51",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_52",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_61",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_62",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_71",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="error_description_72",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="feedback_reveal1",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="feedback_reveal2",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="feedback_reveal3",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="feedback_reveal4",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="feedback_reveal5",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="feedback_reveal6",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="feedback_reveal7",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="logical_error_identification1",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="logical_error_identification2",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="logical_error_identification3",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="logical_error_identification4",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="logical_error_identification5",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="logical_error_identification6",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="logical_error_identification7",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="understandability2",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="understandability3",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="understandability4",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="understandability5",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="understandability6",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersubmission",
            name="understandability7",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
