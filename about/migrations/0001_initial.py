# Generated by Django 4.1.5 on 2023-03-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("full_name", models.CharField(max_length=228)),
                ("position", models.CharField(max_length=228)),
                (
                    "avatar",
                    models.ImageField(blank=True, null=True, upload_to="about/"),
                ),
                ("bio", models.TextField()),
            ],
        ),
    ]
