# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(default=datetime.datetime(2016, 2, 19, 11, 41, 52, 839233, tzinfo=utc), unique=True, max_length=254, verbose_name='user_id'),
            preserve_default=False,
        ),
    ]
