# Generated by Django 4.2.5 on 2024-01-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0009_remove_historicalinterface_active_end_date_test_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinterface',
            name='wait_action',
            field=models.IntegerField(choices=[(1, 'Execute Regardless'), (2, 'Stop/Do Not Execute')]),
        ),
        migrations.AlterField(
            model_name='interface',
            name='wait_action',
            field=models.IntegerField(choices=[(1, 'Execute Regardless'), (2, 'Stop/Do Not Execute')]),
        ),
    ]
