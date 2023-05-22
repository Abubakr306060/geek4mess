# Generated by Django 4.2.1 on 2023-05-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("created", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("PR", "Происшествия"),
                            ("POL", "Политика"),
                            ("SP", "Спорт"),
                            ("KU", "Культура"),
                        ],
                        default="SP",
                        max_length=15,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
            ],
        ),
    ]
