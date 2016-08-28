# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0011_meeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('reportid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('dateperiod', models.CharField(max_length=50, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f\xe8\x8c\x83\xe5\x9b\xb4')),
                ('date', models.DateField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f')),
                ('content', models.TextField(max_length=5000, verbose_name=b'\xe7\xae\x80\xe6\x8a\xa5\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'ordering': ['reportid'],
                'verbose_name': '\u5de5\u4f5c\u7b80\u62a5',
                'verbose_name_plural': '\u5de5\u4f5c\u7b80\u62a5',
            },
        ),
    ]
