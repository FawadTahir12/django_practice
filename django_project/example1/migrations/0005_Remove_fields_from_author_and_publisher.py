# Generated by Django 5.1.5 on 2025-02-02 10:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("example1", "0004_no_defualt_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="author",
            name="firstname",
        ),
        migrations.RemoveField(
            model_name="author",
            name="lastname",
        ),
        migrations.RemoveField(
            model_name="publisher",
            name="firstname",
        ),
        migrations.RemoveField(
            model_name="publisher",
            name="lastname",
        ),
        migrations.AddField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="publisher",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
