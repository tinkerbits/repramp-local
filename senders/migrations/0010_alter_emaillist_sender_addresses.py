# Generated by Django 4.2 on 2023-05-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("senders", "0009_alter_emaillist_sender_addresses"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emaillist",
            name="sender_addresses",
            field=models.CharField(max_length=1000),
        ),
    ]
