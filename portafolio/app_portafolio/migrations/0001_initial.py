# Generated by Django 4.1.3 on 2022-12-08 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="usuario",
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
                ("DNI", models.CharField(default="", max_length=20)),
                ("codigo_usuario", models.CharField(default="", max_length=64)),
                ("clave", models.CharField(default="", max_length=64)),
            ],
        ),
    ]
