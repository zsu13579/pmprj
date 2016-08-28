# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0019_audit_mainstage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditHistory1',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'\xe4\xba\x8b\xe5\xae\x9c')),
                ('incharge', models.CharField(max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('plandate', models.DateField(verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f')),
                ('enddate', models.DateField(null=True, verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('stage', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe4\xba\xa4\xe6\xb5\x81\xe7\xbd\x91\xe7\xab\x99\xe9\x97\xae\xe9\xa2\x98\xe5\x8d\x95\xe6\x94\xb6\xe9\x9b\x86'), (2, b'\xe5\xaf\xb9\xe5\xba\x94\xe5\xb7\xa5\xe5\x8d\x95\xe6\x9f\xa5\xe6\x89\xbe\xe5\x8f\x8a\xe9\x99\x84\xe4\xbb\xb6\xe4\xb8\x8b\xe8\xbd\xbd'), (3, b'\xe5\xaf\xbc\xe5\x87\xba\xe7\xb3\xbb\xe7\xbb\x9f\xe8\xae\xb0\xe5\xbd\x95\xe8\xa1\xa8'), (4, b'\xe6\xa0\xb8\xe5\xaf\xb9')])),
                ('state', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (2, b'\xe6\x9c\xaa\xe5\x90\xaf\xe5\x8a\xa8')])),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(201411\u81f3\u4eca)',
                'verbose_name_plural': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(201411\u81f3\u4eca)',
            },
        ),
        migrations.CreateModel(
            name='AuditHistory2',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'\xe4\xba\x8b\xe5\xae\x9c')),
                ('incharge', models.CharField(max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('plandate', models.DateField(verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f')),
                ('enddate', models.DateField(null=True, verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('stage', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe4\xba\xa4\xe6\xb5\x81\xe7\xbd\x91\xe7\xab\x99\xe9\x97\xae\xe9\xa2\x98\xe5\x8d\x95\xe6\x94\xb6\xe9\x9b\x86'), (2, b'\xe5\xaf\xb9\xe5\xba\x94\xe5\xb7\xa5\xe5\x8d\x95\xe6\x9f\xa5\xe6\x89\xbe\xe5\x8f\x8a\xe9\x99\x84\xe4\xbb\xb6\xe4\xb8\x8b\xe8\xbd\xbd'), (3, b'\xe5\xaf\xbc\xe5\x87\xba\xe7\xb3\xbb\xe7\xbb\x9f\xe8\xae\xb0\xe5\xbd\x95\xe8\xa1\xa8'), (4, b'\xe6\xa0\xb8\xe5\xaf\xb9')])),
                ('state', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (2, b'\xe6\x9c\xaa\xe5\x90\xaf\xe5\x8a\xa8')])),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(2011\u81f3201410)',
                'verbose_name_plural': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(2011\u81f3201410)',
            },
        ),
        migrations.CreateModel(
            name='AuditHistoryStagePercent1',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('stage', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe4\xba\xa4\xe6\xb5\x81\xe7\xbd\x91\xe7\xab\x99\xe9\x97\xae\xe9\xa2\x98\xe5\x8d\x95\xe6\x94\xb6\xe9\x9b\x86'), (2, b'\xe5\xaf\xb9\xe5\xba\x94\xe5\xb7\xa5\xe5\x8d\x95\xe6\x9f\xa5\xe6\x89\xbe\xe5\x8f\x8a\xe9\x99\x84\xe4\xbb\xb6\xe4\xb8\x8b\xe8\xbd\xbd'), (3, b'\xe5\xaf\xbc\xe5\x87\xba\xe7\xb3\xbb\xe7\xbb\x9f\xe8\xae\xb0\xe5\xbd\x95\xe8\xa1\xa8'), (4, b'\xe6\xa0\xb8\xe5\xaf\xb9')])),
                ('percent', models.IntegerField(verbose_name=b'\xe5\x8d\xa0\xe6\x80\xbb\xe5\xb7\xa5\xe4\xbd\x9c\xe9\x87\x8f\xe7\x99\xbe\xe5\x88\x86\xe6\xaf\x94(\xe5\x8d\x95\xe4\xbd\x8d\xef\xbc\x9a%)')),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(201411\u81f3\u4eca)\u5404\u5b50\u9636\u6bb5\u5de5\u4f5c\u91cf\u5360\u6bd4',
                'verbose_name_plural': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(201411\u81f3\u4eca)\u5404\u5b50\u9636\u6bb5\u5de5\u4f5c\u91cf\u5360\u6bd4',
            },
        ),
        migrations.CreateModel(
            name='AuditHistoryStagePercent2',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('stage', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe4\xba\xa4\xe6\xb5\x81\xe7\xbd\x91\xe7\xab\x99\xe9\x97\xae\xe9\xa2\x98\xe5\x8d\x95\xe6\x94\xb6\xe9\x9b\x86'), (2, b'\xe5\xaf\xb9\xe5\xba\x94\xe5\xb7\xa5\xe5\x8d\x95\xe6\x9f\xa5\xe6\x89\xbe\xe5\x8f\x8a\xe9\x99\x84\xe4\xbb\xb6\xe4\xb8\x8b\xe8\xbd\xbd'), (3, b'\xe5\xaf\xbc\xe5\x87\xba\xe7\xb3\xbb\xe7\xbb\x9f\xe8\xae\xb0\xe5\xbd\x95\xe8\xa1\xa8'), (4, b'\xe6\xa0\xb8\xe5\xaf\xb9')])),
                ('percent', models.IntegerField(verbose_name=b'\xe5\x8d\xa0\xe6\x80\xbb\xe5\xb7\xa5\xe4\xbd\x9c\xe9\x87\x8f\xe7\x99\xbe\xe5\x88\x86\xe6\xaf\x94(\xe5\x8d\x95\xe4\xbd\x8d\xef\xbc\x9a%)')),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(2011\u81f3201410)\u5404\u5b50\u9636\u6bb5\u5de5\u4f5c\u91cf\u5360\u6bd4',
                'verbose_name_plural': '\u8865\u5145\u5386\u53f2\u8bb0\u5f55(2011\u81f3201410)\u5404\u5b50\u9636\u6bb5\u5de5\u4f5c\u91cf\u5360\u6bd4',
            },
        ),
        migrations.CreateModel(
            name='AuditOverview',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('stage', models.IntegerField(default=1, verbose_name=b'\xe4\xb8\xbb\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe8\xa7\xa3\xe5\x86\xb3\xe9\x81\x97\xe7\x95\x99\xe9\x97\xae\xe9\xa2\x98'), (2, b'\xe4\xbc\x98\xe5\x8c\x96\xe5\xb1\x80\xe6\x95\xb0\xe6\x8d\xae\xe6\xb5\x81\xe7\xa8\x8b'), (3, b'\xe8\xa1\xa5\xe5\x85\x85\xe5\x8e\x86\xe5\x8f\xb2\xe8\xae\xb0\xe5\xbd\x95(201411\xe8\x87\xb3\xe4\xbb\x8a)'), (4, b'\xe8\xa1\xa5\xe5\x85\x85\xe5\x8e\x86\xe5\x8f\xb2\xe8\xae\xb0\xe5\xbd\x95(2011\xe8\x87\xb3201410)')])),
                ('incharge', models.CharField(max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('plandate', models.DateField(verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f')),
                ('enddate', models.DateField(null=True, verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('state', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (2, b'\xe6\x9c\xaa\xe5\x90\xaf\xe5\x8a\xa8')])),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u5ba1\u8ba1\u5de5\u4f5c\u603b\u4f53\u60c5\u51b5',
                'verbose_name_plural': '\u5ba1\u8ba1\u5de5\u4f5c\u603b\u4f53\u60c5\u51b5',
            },
        ),
        migrations.CreateModel(
            name='AuditProblem',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'\xe4\xba\x8b\xe5\xae\x9c')),
                ('incharge', models.CharField(max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('plandate', models.DateField(verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f')),
                ('enddate', models.DateField(null=True, verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('stage', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'56\xe4\xb8\xaaOA\xe6\x96\x87'), (2, b'82\xe4\xb8\xaaOA\xe6\x96\x87'), (3, b'\xe5\x8d\x8f\xe8\xb0\x83\xe9\x9b\x86\xe5\x9b\xa2\xe4\xba\xa4\xe6\xb5\x81\xe7\xbd\x91\xe7\xab\x99\xe8\xa1\xa5\xe5\x8f\x91')])),
                ('state', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (2, b'\xe6\x9c\xaa\xe5\x90\xaf\xe5\x8a\xa8')])),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u89e3\u51b3\u9057\u7559\u95ee\u9898',
                'verbose_name_plural': '\u89e3\u51b3\u9057\u7559\u95ee\u9898',
            },
        ),
        migrations.CreateModel(
            name='AuditProblemStagePercent',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('stage', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'56\xe4\xb8\xaaOA\xe6\x96\x87'), (2, b'82\xe4\xb8\xaaOA\xe6\x96\x87'), (3, b'\xe5\x8d\x8f\xe8\xb0\x83\xe9\x9b\x86\xe5\x9b\xa2\xe4\xba\xa4\xe6\xb5\x81\xe7\xbd\x91\xe7\xab\x99\xe8\xa1\xa5\xe5\x8f\x91')])),
                ('percent', models.IntegerField(verbose_name=b'\xe5\x8d\xa0\xe6\x80\xbb\xe5\xb7\xa5\xe4\xbd\x9c\xe9\x87\x8f\xe7\x99\xbe\xe5\x88\x86\xe6\xaf\x94(\xe5\x8d\x95\xe4\xbd\x8d\xef\xbc\x9a%)')),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u89e3\u51b3\u9057\u7559\u95ee\u9898\u5404\u5b50\u9636\u6bb5\u5de5\u4f5c\u91cf\u5360\u6bd4',
                'verbose_name_plural': '\u89e3\u51b3\u9057\u7559\u95ee\u9898\u5404\u5b50\u9636\u6bb5\u5de5\u4f5c\u91cf\u5360\u6bd4',
            },
        ),
        migrations.CreateModel(
            name='AuditProcedure',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'\xe4\xba\x8b\xe5\xae\x9c')),
                ('incharge', models.CharField(max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('plandate', models.DateField(verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f')),
                ('enddate', models.DateField(null=True, verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('stage', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe6\x94\xb9\xe9\x80\xa0\xe4\xba\xa4\xe6\xb5\x81\xe7\xbd\x91\xe7\xab\x99'), (2, b'\xe6\x94\xb9\xe9\x80\xa0\xe5\xb7\xa5\xe5\x8d\x95\xe7\xb3\xbb\xe7\xbb\x9f'), (3, b'\xe6\x96\xb0\xe5\xb1\x80\xe6\x95\xb0\xe6\x8d\xae\xe6\xb5\x81\xe7\xa8\x8b\xe6\x89\x8b\xe5\x86\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe5\xae\x9e\xe6\x96\xbd'), (4, b'\xe6\x95\xb4\xe6\x94\xb9\xe5\x9b\xbd\xe9\x99\x85\xe5\x8f\xa3\xe6\x9d\xa5\xe8\xae\xbf\xe9\x95\xbf\xe9\x80\x94\xe8\xb4\xb9\xe7\x8e\x87\xe6\x89\xb9\xe4\xbb\xb7\xe9\x80\xbb\xe8\xbe\x91\xe5\x8f\x8a\xe7\x95\x8c\xe9\x9d\xa2\xe5\xb1\x95\xe7\xa4\xba')])),
                ('state', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (1, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (2, b'\xe6\x9c\xaa\xe5\x90\xaf\xe5\x8a\xa8')])),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u4f18\u5316\u5c40\u6570\u636e\u6d41\u7a0b',
                'verbose_name_plural': '\u4f18\u5316\u5c40\u6570\u636e\u6d41\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='AuditProcedureStagePercent',
            fields=[
                ('itemid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('stage', models.IntegerField(verbose_name=b'\xe5\xad\x90\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe6\x94\xb9\xe9\x80\xa0\xe4\xba\xa4\xe6\xb5\x81\xe7\xbd\x91\xe7\xab\x99'), (2, b'\xe6\x94\xb9\xe9\x80\xa0\xe5\xb7\xa5\xe5\x8d\x95\xe7\xb3\xbb\xe7\xbb\x9f'), (3, b'\xe6\x96\xb0\xe5\xb1\x80\xe6\x95\xb0\xe6\x8d\xae\xe6\xb5\x81\xe7\xa8\x8b\xe6\x89\x8b\xe5\x86\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe5\xae\x9e\xe6\x96\xbd'), (4, b'\xe6\x95\xb4\xe6\x94\xb9\xe5\x9b\xbd\xe9\x99\x85\xe5\x8f\xa3\xe6\x9d\xa5\xe8\xae\xbf\xe9\x95\xbf\xe9\x80\x94\xe8\xb4\xb9\xe7\x8e\x87\xe6\x89\xb9\xe4\xbb\xb7\xe9\x80\xbb\xe8\xbe\x91\xe5\x8f\x8a\xe7\x95\x8c\xe9\x9d\xa2\xe5\xb1\x95\xe7\xa4\xba')])),
                ('percent', models.IntegerField(verbose_name=b'\xe5\x8d\xa0\xe6\x80\xbb\xe5\xb7\xa5\xe4\xbd\x9c\xe9\x87\x8f\xe7\x99\xbe\xe5\x88\x86\xe6\xaf\x94(\xe5\x8d\x95\xe4\xbd\x8d\xef\xbc\x9a%)')),
                ('note', models.TextField(max_length=20000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'ordering': ['itemid'],
                'verbose_name': '\u4f18\u5316\u5c40\u6570\u636e\u6d41\u7a0b\u5404\u5b50\u9636\u6bb5\u5de5\u4f5c\u91cf\u5360\u6bd4',
                'verbose_name_plural': '\u4f18\u5316\u5c40\u6570\u636e\u6d41\u7a0b\u5404\u5b50\u9636\u6bb5\u5de5\u4f5c\u91cf\u5360\u6bd4',
            },
        ),
        migrations.DeleteModel(
            name='Audit',
        ),
    ]
