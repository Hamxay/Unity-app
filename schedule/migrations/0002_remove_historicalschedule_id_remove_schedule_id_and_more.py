# Generated by Django 4.2.5 on 2024-01-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalschedule',
            name='id',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='id',
        ),
        migrations.AlterField(
            model_name='historicalschedule',
            name='Code',
            field=models.BigIntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='Code',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
