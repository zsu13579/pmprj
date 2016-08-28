# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workitem',
            fields=[
                ('itemid', models.IntegerField(max_length=50, serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('category', models.CharField(max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab')),
                ('progress', models.TextField(max_length=2000, verbose_name=b'\xe5\xae\x8c\xe6\x88\x90\xe6\x83\x85\xe5\x86\xb5')),
                ('plan', models.TextField(max_length=2000, verbose_name=b'\xe5\x90\x8e\xe7\xbb\xad\xe5\xb7\xa5\xe4\xbd\x9c')),
                ('state', models.IntegerField(max_length=3, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u91cd\u70b9\u5de5\u4f5c\u8fdb\u5c55\u60c5\u51b5',
            },
        ),
    ]
