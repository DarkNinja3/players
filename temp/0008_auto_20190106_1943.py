# Generated by Django 2.1.4 on 2019-01-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_auto_20190106_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mins_left',
            field=models.FloatField(blank='true', default=78, null='true'),
        ),
    ]
