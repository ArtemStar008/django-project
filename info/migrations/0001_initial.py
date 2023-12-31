# Generated by Django 4.2.6 on 2023-10-13 22:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InfoBlog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("name", models.CharField(max_length=30)),
                ("rating", models.PositiveSmallIntegerField()),
                ("price", models.FloatField()),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
    ]
