# Generated by Django 4.0.3 on 2022-04-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menu_latest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='latest_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
