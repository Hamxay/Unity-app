# Generated by Django 4.2.5 on 2023-11-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalattribute',
            name='skip_save',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='historicalattribute',
            name='code',
            field=models.IntegerField(db_index=True),
        ),
    ]
