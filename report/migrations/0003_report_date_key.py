# Generated by Django 4.2.5 on 2024-08-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_alter_report_created_by_alter_report_updated_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date_key',
            field=models.CharField(default='Datekey', max_length=250),
            preserve_default=False,
        ),
    ]