# Generated by Django 3.2.3 on 2021-05-30 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_rbbackup', '0005_auto_20210326_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='routers',
            name='dev_info',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='RouterBackups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file_name', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=15)),
                ('file_ext', models.CharField(blank=True, max_length=15, null=True)),
                ('time_backup', models.DecimalField(decimal_places=1, default=0, max_digits=6)),
                ('dev_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='router_backups', to='api_rbbackup.routers')),
            ],
            options={
                'db_table': 'routers_backups',
            },
        ),
    ]
