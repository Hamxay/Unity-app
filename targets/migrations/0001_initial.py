# Generated by Django 4.2.5 on 2023-09-13 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kpi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Targets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('base_line', models.BigIntegerField(blank=True, null=True)),
                ('lower_bound', models.BigIntegerField()),
                ('upper_bound', models.BigIntegerField()),
                ('effective_start_date', models.DateTimeField()),
                ('effective_end_date', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('kpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kpi.kpi')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
                'abstract': False,
            },
        ),
    ]
