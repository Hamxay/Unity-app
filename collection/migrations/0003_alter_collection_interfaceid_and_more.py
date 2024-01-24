# Generated by Django 4.2.5 on 2024-01-26 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0010_alter_historicalinterface_wait_action_and_more'),
        ('collection', '0002_remove_collection_id_remove_historicalcollection_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='interfaceid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.interface'),
        ),
        migrations.AlterField(
            model_name='historicalcollection',
            name='interfaceid',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='interface.interface'),
        ),
    ]