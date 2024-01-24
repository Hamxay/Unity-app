# Generated by Django 4.2.5 on 2024-01-24 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0005_alter_class_ignoreoningest_and_more'),
        ('attribute', '0003_remove_attribute_id_remove_historicalattribute_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.class'),
        ),
        migrations.AlterField(
            model_name='historicalattribute',
            name='class_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='classapp.class'),
        ),
    ]