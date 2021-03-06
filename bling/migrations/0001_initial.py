# Generated by Django 2.0.dev20170426002136 on 2017-04-26 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2017, 4, 26, 15, 10, 25, 448166, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
