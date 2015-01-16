# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'name')),
                ('surname', models.CharField(max_length=200, verbose_name=b'surname')),
                ('birth', models.DateField(verbose_name=b'birth')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b't\xc3\xadtulo')),
                ('isbn', models.CharField(max_length=13, verbose_name=b'isbn')),
                ('authors', models.ManyToManyField(to='Books.Author')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
            bases=(models.Model,),
        ),
    ]
