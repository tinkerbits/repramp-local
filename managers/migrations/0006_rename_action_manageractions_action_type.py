# Generated by Django 4.2.1 on 2023-05-25 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("managers", "0005_alter_manageractions_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="manageractions",
            old_name="action",
            new_name="action_type",
        ),
    ]
