# Generated by Django 4.2.5 on 2024-01-25 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_remove_collection_precedingcollectionid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='executiontriggerrule',
            field=models.SmallIntegerField(choices=[(1, 'Success'), (2, 'Complete')]),
        ),
        migrations.AlterField(
            model_name='historicalcollection',
            name='executiontriggerrule',
            field=models.SmallIntegerField(choices=[(1, 'Success'), (2, 'Complete')]),
        ),
    ]
