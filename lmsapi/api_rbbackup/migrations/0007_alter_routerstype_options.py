# Generated by Django 3.2.12 on 2022-03-29 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rbbackup', '0006_auto_20210530_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='routerstype',
            options={'ordering': ['type']},
        ),
    ]
