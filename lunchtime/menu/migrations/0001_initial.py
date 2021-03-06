# Generated by Django 3.2.12 on 2022-04-02 06:55

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('food_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('menu', models.TextField()),
                ('latest_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
