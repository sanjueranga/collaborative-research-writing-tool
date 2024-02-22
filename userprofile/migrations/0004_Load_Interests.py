# Generated by Django 4.2.10 on 2024-02-21 14:48

from django.db import migrations
from django.core.management import call_command


def load_initial_data(apps, schema_editor):
    call_command(
        "loaddata",
        "interests.json",
        app_label="userprofile",
    )


def unload_initial_data(apps, schema_editor):
    interestModel = apps.get_model("userprofile", "Interest")
    interestModel.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0003_Load_Experience"),
    ]

    operations = [
        migrations.RunPython(load_initial_data, unload_initial_data),
    ]
