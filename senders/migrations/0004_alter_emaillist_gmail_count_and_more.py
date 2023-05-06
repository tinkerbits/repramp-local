# Generated by Django 4.2 on 2023-05-05 08:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("senders", "0003_alter_emaillist_gmail_count_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emaillist",
            name="gmail_count",
            field=models.PositiveSmallIntegerField(
                default=0,
                validators=[django.core.validators.MaxValueValidator(limit_value=3)],
            ),
        ),
        migrations.AlterField(
            model_name="emaillist",
            name="microsoft_count",
            field=models.PositiveSmallIntegerField(
                default=0,
                validators=[django.core.validators.MaxValueValidator(limit_value=2)],
            ),
        ),
        migrations.AlterField(
            model_name="emaillist",
            name="other_count",
            field=models.PositiveSmallIntegerField(
                default=0,
                validators=[django.core.validators.MaxValueValidator(limit_value=1)],
            ),
        ),
        migrations.AlterField(
            model_name="emaillist",
            name="yahoo_count",
            field=models.PositiveSmallIntegerField(
                default=0,
                validators=[django.core.validators.MaxValueValidator(limit_value=2)],
            ),
        ),
    ]