# Generated by Django 2.1.4 on 2019-01-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0020_auto_20190106_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mins_left',
            field=models.FloatField(blank='true', default=51, null='true'),
        ),
    ]