# Generated by Django 4.2.5 on 2023-09-27 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("robots", "0007_alter_robot_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="robot",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime.now, verbose_name="Создан"
            ),
        ),
    ]
