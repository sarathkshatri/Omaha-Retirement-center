# Generated by Django 2.1.5 on 2019-12-17 04:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ORC', '0003_auto_20191216_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomallotment',
            name='allotment_enddate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 4, 59, 56, 259873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roomallotment',
            name='allotment_startdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 4, 59, 56, 259840, tzinfo=utc)),
        ),
    ]
