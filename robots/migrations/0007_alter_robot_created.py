# Generated by Django 4.2.5 on 2023-09-25 14:54

import datetime
from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0006_alter_robot_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]