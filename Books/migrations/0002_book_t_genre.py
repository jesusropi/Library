# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='t_genre',
            field=models.CharField(default=datetime.datetime(2015, 1, 16, 17, 52, 48, 839353, tzinfo=utc), max_length=1, choices=[(b'E', b'Epica'), (b'L', b'Lirica')]),
            preserve_default=False,
        ),
    ]
