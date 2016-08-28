#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Workitem(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    category = models.CharField(max_length=50, verbose_name='类别')
    progress = models.TextField(max_length=2000, verbose_name='完成情况')
    plan = models.TextField(max_length=2000, verbose_name='后续工作')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成')), verbose_name='状态')

    class Meta:
        verbose_name = '重点工作进展情况'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class Meeting(models.Model):
    meetingid = models.IntegerField(primary_key=True, verbose_name='序号')
    date = models.DateField(verbose_name='日期')
    memo = models.TextField(max_length=5000, verbose_name='会议纪要')
    attender = models.TextField(max_length=1000, verbose_name='参会人员')
    type = models.IntegerField(choices=((1,'日常交流'),(2,'集团会议'),(3,'高层会议')))

    class Meta:
        verbose_name = '会议情况'
        verbose_name_plural = verbose_name
        ordering = ['-date']

class Report(models.Model):
    reportid = models.IntegerField(primary_key=True, verbose_name='序号')
    dateperiod = models.CharField(max_length=50, verbose_name='日期范围')
    date = models.DateField(verbose_name='发布日期')
    content = models.TextField(max_length=50000, verbose_name='简报内容')
    file = models.FileField(upload_to='report/', blank=True, null=True, verbose_name='简报文件')
    filename = models.CharField(max_length=500, blank=True, null=True, verbose_name='简报文件名称')

    class Meta:
        verbose_name = '工作简报'
        verbose_name_plural = verbose_name
        ordering = ['-reportid']

class Audit(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    mainstage = models.IntegerField(
        choices=((0, '总体计划'), (1, '解决遗留问题'), (2, '优化局数据流程'), (3, '补充历史记录(201411至今)'), (4, '补充历史记录(2011至201410)')),
        default=1, verbose_name='主阶段')
    stage = models.IntegerField(choices=((0, '局数据维护新流程手册编写'), (1, '交流网站问题单收集'), (2, '对应工单查找及附件下载'), (3, '导出系统记录表'), (4, '核对')), verbose_name='子阶段')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '审计工作进展情况'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class AuditDashboard(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    mainstage = models.IntegerField(choices=((0, '总体计划'), (1, '解决遗留问题'), (2, '优化局数据流程'), (3, '补充历史记录(201411至今)'), (4, '补充历史记录(2011至201410)')), default=1, verbose_name='主阶段')
    stage = models.IntegerField(choices=((1, '交流网站问题单收集'), (2, '对应工单查找及附件下载'), (3, '导出系统记录表'), (4, '核对')), verbose_name='子阶段')
    percent = models.IntegerField(verbose_name='完成百分比(单位：%)')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '审计工作完成率'
        verbose_name_plural = verbose_name
        ordering = ['itemid']