# Generated by Django 2.1.4 on 2019-01-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20190104_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='mins_left',
            field=models.FloatField(blank='true', default=87, null='true'),
        ),
    ]
