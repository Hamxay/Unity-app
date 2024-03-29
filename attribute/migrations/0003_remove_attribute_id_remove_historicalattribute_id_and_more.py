# Generated by Django 4.2.5 on 2024-01-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0002_historicalattribute_skip_save_alter_attribute_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='id',
        ),
        migrations.RemoveField(
            model_name='historicalattribute',
            name='id',
        ),
        migrations.AlterField(
            model_name='attribute',
            name='code',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='historicalattribute',
            name='code',
            field=models.BigIntegerField(blank=True, db_index=True),
        ),
    ]
