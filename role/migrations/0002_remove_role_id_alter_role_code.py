# Generated by Django 4.2.5 on 2024-01-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='id',
        ),
        migrations.AlterField(
            model_name='role',
            name='code',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
