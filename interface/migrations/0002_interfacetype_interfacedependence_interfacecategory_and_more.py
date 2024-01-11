# Generated by Django 4.2.5 on 2023-12-11 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterfaceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'InterfaceType',
            },
        ),
        migrations.CreateModel(
            name='InterfaceDependence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('code', models.IntegerField(unique=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('dependent_on_interface', models.ForeignKey(db_column='DependentOnInterfaceId', on_delete=django.db.models.deletion.CASCADE, related_name='dependent_interface', to='interface.interface')),
                ('interface_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.interface')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'InterfaceDependence',
            },
        ),
        migrations.CreateModel(
            name='InterfaceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'InterfaceCategory',
            },
        ),
        migrations.AlterField(
            model_name='historicalinterface',
            name='interface_category_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='interface.interfacecategory'),
        ),
        migrations.AlterField(
            model_name='historicalinterface',
            name='interface_type_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='interface.interfacetype'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='interface_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.interfacecategory'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='interface_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.interfacetype'),
        ),
        migrations.AddConstraint(
            model_name='interfacetype',
            constraint=models.UniqueConstraint(fields=('code',), name='UQ__InterfaceType__Code'),
        ),
        migrations.AddConstraint(
            model_name='interfacedependence',
            constraint=models.UniqueConstraint(fields=('code',), name='UQ__InterfaceDependence__Code'),
        ),
        migrations.AddConstraint(
            model_name='interfacecategory',
            constraint=models.UniqueConstraint(fields=('code',), name='UQ__InterfaceCategory__Code'),
        ),
    ]
