# Generated by Django 2.1.4 on 2019-01-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0024_auto_20190107_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mins_left',
            field=models.FloatField(blank='true', default=0, null='true'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank='true', default='pass12', max_length=30, null='true'),
        ),
    ]
