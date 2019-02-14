# Generated by Django 2.1.4 on 2019-01-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(max_length=50)),
                ('real_name', models.CharField(max_length=120)),
                ('photo', models.BinaryField(blank='true', null='true')),
                ('email', models.EmailField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mins_left', models.IntegerField(blank='true', null='true')),
            ],
        ),
    ]
