# Generated by Django 4.2.5 on 2024-01-30 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_remove_historicalschedule_id_remove_schedule_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalschedule',
            name='Frequency',
            field=models.IntegerField(choices=[(0, 'Once'), (1, 'Daily'), (2, 'Weekly'), (3, 'Monthly'), (4, 'Monthly-Relative')]),
        ),
        migrations.AlterField(
            model_name='historicalschedule',
            name='FrequencyRelativeInterval',
            field=models.IntegerField(choices=[(0, 'Unused'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Last')]),
        ),
        migrations.AlterField(
            model_name='historicalschedule',
            name='FrequencySubDayType',
            field=models.IntegerField(choices=[(1, 'Minutes'), (2, 'Hourly')]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='Frequency',
            field=models.IntegerField(choices=[(0, 'Once'), (1, 'Daily'), (2, 'Weekly'), (3, 'Monthly'), (4, 'Monthly-Relative')]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='FrequencyRelativeInterval',
            field=models.IntegerField(choices=[(0, 'Unused'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Last')]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='FrequencySubDayType',
            field=models.IntegerField(choices=[(1, 'Minutes'), (2, 'Hourly')]),
        ),
    ]