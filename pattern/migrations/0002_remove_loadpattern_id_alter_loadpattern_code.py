# Generated by Django 4.2.5 on 2024-01-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loadpattern',
            name='id',
        ),
        migrations.AlterField(
            model_name='loadpattern',
            name='code',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
