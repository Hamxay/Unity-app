# Generated by Django 4.2.5 on 2024-01-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='id',
        ),
        migrations.RemoveField(
            model_name='historicalclass',
            name='id',
        ),
        migrations.AlterField(
            model_name='class',
            name='Code',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='historicalclass',
            name='Code',
            field=models.BigIntegerField(blank=True, db_index=True),
        ),
    ]
