# Generated by Django 4.2.3 on 2023-09-01 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "Scname",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("Scprincipal", models.CharField(max_length=100)),
                ("Sclocation", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("Sname", models.CharField(max_length=100)),
                ("Sid", models.IntegerField()),
                (
                    "Scname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.school"
                    ),
                ),
            ],
        ),
    ]
