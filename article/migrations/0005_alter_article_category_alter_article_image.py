# Generated by Django 4.1.5 on 2023-03-30 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0004_alter_subcontent_article_alter_subcontent_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="article.category",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(upload_to="article/"),
        ),
    ]
