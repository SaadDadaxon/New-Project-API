# Generated by Django 4.1.5 on 2023-02-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0002_alter_contact_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.CharField(max_length=17),
        ),
    ]