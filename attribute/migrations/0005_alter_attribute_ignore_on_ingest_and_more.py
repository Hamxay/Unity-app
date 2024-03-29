# Generated by Django 4.2.5 on 2024-01-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0004_alter_attribute_class_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='ignore_on_ingest',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='is_nullable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='is_primary_key',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='is_snapshot_key',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalattribute',
            name='ignore_on_ingest',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalattribute',
            name='is_nullable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalattribute',
            name='is_primary_key',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalattribute',
            name='is_snapshot_key',
            field=models.BooleanField(default=False),
        ),
    ]
