# Generated by Django 4.2 on 2023-05-07 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("managers", "0003_alter_manageractions_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="manageractions",
            old_name="comments",
            new_name="comment",
        ),
    ]
