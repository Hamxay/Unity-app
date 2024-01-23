# Generated by Django 4.2.5 on 2024-01-22 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0007_rename_active_end_date_historicalinterface_active_end_date_test_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalinterface',
            name='active_end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='historicalinterface',
            name='active_start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='interface',
            name='active_end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='interface',
            name='active_start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]