# Generated by Django 4.2.5 on 2023-12-21 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classapp', '0001_initial'),
        ('pattern', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('Code', models.IntegerField()),
                ('Name', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=250, null=True)),
                ('PipelineName', models.CharField(max_length=128)),
                ('PipelineParameters', models.CharField(max_length=2000, null=True)),
                ('SubPipelineParameters', models.CharField(max_length=2000, null=True)),
                ('DeduplicateSource', models.CharField(max_length=1, null=True)),
                ('Priority', models.IntegerField(null=True)),
                ('ClassId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.class')),
                ('CollectionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.collection')),
                ('LoadPatternId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pattern.loadpattern')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Task',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTask',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('skip_save', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('updated_date', models.DateTimeField(blank=True, editable=False)),
                ('Code', models.IntegerField()),
                ('Name', models.CharField(max_length=128)),
                ('Description', models.CharField(max_length=250, null=True)),
                ('PipelineName', models.CharField(max_length=128)),
                ('PipelineParameters', models.CharField(max_length=2000, null=True)),
                ('SubPipelineParameters', models.CharField(max_length=2000, null=True)),
                ('DeduplicateSource', models.CharField(max_length=1, null=True)),
                ('Priority', models.IntegerField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('ClassId', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='classapp.class')),
                ('CollectionId', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='collection.collection')),
                ('LoadPatternId', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pattern.loadpattern')),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical task',
                'verbose_name_plural': 'historical tasks',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
