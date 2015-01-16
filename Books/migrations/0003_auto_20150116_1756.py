# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_book_t_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='t_genre',
            field=models.CharField(default=b'L', max_length=1, choices=[(b'E', b'Epica'), (b'L', b'Lirica')]),
            preserve_default=True,
        ),
    ]
