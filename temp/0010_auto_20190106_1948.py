# Generated by Django 2.1.4 on 2019-01-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_auto_20190106_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mins_left',
            field=models.FloatField(blank='true', default=56, null='true'),
        ),
    ]
