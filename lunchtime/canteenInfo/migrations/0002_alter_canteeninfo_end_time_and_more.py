# Generated by Django 4.0.1 on 2022-04-03 00:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('canteenInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canteeninfo',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2022, 4, 3, 1, 18, 55, 358359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='canteeninfo',
            name='last_scan_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 0, 48, 55, 358359, tzinfo=utc)),
        ),
    ]
