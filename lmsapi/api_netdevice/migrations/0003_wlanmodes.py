# Generated by Django 3.2.13 on 2022-07-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_netdevice', '0002_hwtypes_netcontypes_nmsgroups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wlanmodes',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('apmode', models.CharField(max_length=32)),
                ('popis', models.CharField(blank=True, max_length=255, null=True)),
                ('nas_type', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'wlanmodes',
                'managed': False,
            },
        ),
    ]
