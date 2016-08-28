# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0024_bossaccept_bossoperationprocess_bosstestcase'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.TextField(max_length=500)),
                ('intime', models.DateTimeField(default=b'2016-03-01 0:0:0')),
                ('deletetag', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['deletetag'],
                'db_table': 'todolist',
            },
        ),
    ]
