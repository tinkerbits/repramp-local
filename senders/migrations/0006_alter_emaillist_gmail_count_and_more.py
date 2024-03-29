# Generated by Django 4.2 on 2023-05-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("senders", "0005_alter_emaillist_gmail_count_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emaillist",
            name="gmail_count",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="emaillist",
            name="microsoft_count",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="emaillist",
            name="other_count",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="emaillist",
            name="yahoo_count",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
