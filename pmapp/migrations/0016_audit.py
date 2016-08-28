# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0015_report_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'\xe4\xba\x8b\xe5\xae\x9c')),
                ('incharge', models.CharField(max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('progress', models.TextField(max_length=2000, verbose_name=b'\xe5\xae\x8c\xe6\x88\x90\xe6\x83\x85\xe5\x86\xb5')),
                ('plandate', models.DateField(verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f')),
                ('enddate', models.DateField(verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f')),
                ('stage', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe9\x98\xb6\xe6\xae\xb5', choices=[(0, b'\xe4\xba\xa4\xe6\xb5\x81\xe7\xbd\x91\xe7\xab\x99\xe9\x97\xae\xe9\xa2\x98\xe5\x8d\x95\xe6\x94\xb6\xe9\x9b\x86'), (1, b'\xe5\xaf\xb9\xe5\xba\x94\xe5\xb7\xa5\xe5\x8d\x95\xe6\x9f\xa5\xe6\x89\xbe\xe5\x8f\x8a\xe9\x99\x84\xe4\xbb\xb6\xe4\xb8\x8b\xe8\xbd\xbd'), (2, b'\xe5\xaf\xbc\xe5\x87\xba\xe7\xb3\xbb\xe7\xbb\x9f\xe8\xae\xb0\xe5\xbd\x95\xe8\xa1\xa8'), (3, b'\xe6\xa0\xb8\xe5\xaf\xb9')])),
                ('state', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u5ba1\u8ba1\u5de5\u4f5c\u8fdb\u5c55\u60c5\u51b5',
                'verbose_name_plural': '\u5ba1\u8ba1\u5de5\u4f5c\u8fdb\u5c55\u60c5\u51b5',
            },
        ),
    ]
