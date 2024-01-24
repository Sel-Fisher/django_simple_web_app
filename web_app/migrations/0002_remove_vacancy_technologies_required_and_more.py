# Generated by Django 5.0.1 on 2024-01-24 01:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vacancy",
            name="technologies_required",
        ),
        migrations.AddField(
            model_name="vacancy",
            name="technologies_required",
            field=models.ManyToManyField(
                related_name="vacancy", to="web_app.technology"
            ),
        ),
    ]
