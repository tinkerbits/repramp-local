# Generated by Django 4.2 on 2023-05-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("managers", "0004_rename_comments_manageractions_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manageractions",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("accepted", "accepted"), ("rejected", "rejected")],
                max_length=20,
                null=True,
            ),
        ),
    ]