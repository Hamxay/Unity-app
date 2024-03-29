# Generated by Django 4.2.5 on 2023-11-09 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalAttribute',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('updated_date', models.DateTimeField(blank=True, editable=False)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('code', models.IntegerField()),
                ('class_id', models.IntegerField()),
                ('source_name', models.CharField(max_length=128)),
                ('target_name', models.CharField(max_length=128)),
                ('source_description', models.CharField(max_length=250, null=True)),
                ('target_description', models.CharField(max_length=250, null=True)),
                ('source_ordinal_position', models.IntegerField()),
                ('target_ordinal_position', models.IntegerField()),
                ('source_data_type', models.CharField(max_length=128)),
                ('target_data_type', models.CharField(max_length=128)),
                ('source_max_length', models.IntegerField(null=True)),
                ('target_max_length', models.IntegerField(null=True)),
                ('source_precision', models.IntegerField(null=True)),
                ('target_precision', models.IntegerField(null=True)),
                ('source_scale', models.IntegerField(null=True)),
                ('target_scale', models.IntegerField(null=True)),
                ('is_primary_key', models.CharField(max_length=1)),
                ('is_snapshot_key', models.CharField(max_length=1)),
                ('is_nullable', models.CharField(max_length=1)),
                ('ignore_on_ingest', models.CharField(max_length=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical attribute',
                'verbose_name_plural': 'historical attributes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('code', models.IntegerField()),
                ('class_id', models.IntegerField()),
                ('source_name', models.CharField(max_length=128)),
                ('target_name', models.CharField(max_length=128)),
                ('source_description', models.CharField(max_length=250, null=True)),
                ('target_description', models.CharField(max_length=250, null=True)),
                ('source_ordinal_position', models.IntegerField()),
                ('target_ordinal_position', models.IntegerField()),
                ('source_data_type', models.CharField(max_length=128)),
                ('target_data_type', models.CharField(max_length=128)),
                ('source_max_length', models.IntegerField(null=True)),
                ('target_max_length', models.IntegerField(null=True)),
                ('source_precision', models.IntegerField(null=True)),
                ('target_precision', models.IntegerField(null=True)),
                ('source_scale', models.IntegerField(null=True)),
                ('target_scale', models.IntegerField(null=True)),
                ('is_primary_key', models.CharField(max_length=1)),
                ('is_snapshot_key', models.CharField(max_length=1)),
                ('is_nullable', models.CharField(max_length=1)),
                ('ignore_on_ingest', models.CharField(max_length=1)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
                'abstract': False,
            },
        ),
    ]
