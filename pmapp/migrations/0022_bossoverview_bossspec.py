# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0021_auto_20160716_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='BossOverview',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('stage', models.IntegerField(default=1, verbose_name=b'\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe9\x9c\x80\xe6\xb1\x82\xe7\xbc\x96\xe5\x86\x99'), (2, b'\xe9\xaa\x8c\xe6\x94\xb6\xe6\xa1\x88\xe4\xbe\x8b\xe7\xbc\x96\xe5\x86\x99'), (3, b'\xe9\xaa\x8c\xe6\x94\xb6\xe6\xb5\x8b\xe8\xaf\x95'), (4, b'\xe4\xb8\x8a\xe7\xba\xbf\xe8\xb7\x9f\xe8\xb8\xaa')])),
                ('incharge', models.CharField(max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('plandate', models.DateField(verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f')),
                ('enddate', models.DateField(null=True, verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('state', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (2, b'\xe6\x9c\xaa\xe5\x90\xaf\xe5\x8a\xa8')])),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u56fd\u6f2b\u6d41\u7a0b\u4f18\u5316\u5de5\u4f5c\u603b\u4f53\u60c5\u51b5',
                'verbose_name_plural': '\u56fd\u6f2b\u6d41\u7a0b\u4f18\u5316\u5de5\u4f5c\u603b\u4f53\u60c5\u51b5',
            },
        ),
        migrations.CreateModel(
            name='BossSpec',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'\xe4\xba\x8b\xe5\xae\x9c')),
                ('incharge', models.CharField(max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('plandate', models.DateField(verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f')),
                ('enddate', models.DateField(null=True, verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('module', models.IntegerField(verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd\xe6\xa8\xa1\xe5\x9d\x97', choices=[(1, b'\xe5\x8a\x9f\xe8\x83\xbd\xe5\xbc\x80\xe9\x80\x9a'), (2, b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\xa1\xe7\x90\x86'), (3, b'\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x8a\x9e\xe7\x90\x86'), (4, b'\xe8\xae\xa1\xe8\xb4\xb9'), (5, b'\xe6\x8f\x90\xe9\x86\x92'), (6, b'\xe7\x9f\xad\xe4\xbf\xa1\xe7\xae\xa1\xe7\x90\x86')])),
                ('state', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (2, b'\xe6\x9c\xaa\xe5\x90\xaf\xe5\x8a\xa8')])),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(2011\u81f3201410)',
                'verbose_name_plural': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(2011\u81f3201410)',
            },
        ),
    ]
