# Generated by Django 4.2.5 on 2023-09-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin')], default=1, verbose_name='role'),
        ),
    ]
