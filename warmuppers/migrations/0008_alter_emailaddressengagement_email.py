# Generated by Django 4.2 on 2023-05-19 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("warmuppers", "0007_emailaddressengagement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailaddressengagement",
            name="email",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="engagement_emails",
                to="warmuppers.emailaddress",
            ),
        ),
    ]
