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

class AuditOverview(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    stage = models.IntegerField(
        choices=((1, '解决遗留问题'), (2, '优化局数据流程'), (3, '补充历史记录(201411至今)'), (4, '补充历史记录(2011至201410)')),
        default=1, verbose_name='主阶段')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '审计工作总体情况'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class AuditProblem(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    stage = models.IntegerField(
        choices=((1, '56个OA文'), (2, '82个OA文'), (3, '协调集团交流网站补发'), (4, '修正系统记录、完善系统逻辑')), verbose_name='子阶段')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '解决遗留问题'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class AuditProcedure(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    stage = models.IntegerField(
        choices=((1, '改造交流网站'), (2, '改造工单系统'), (3, '新局数据流程手册更新实施'), (4, '整改国际口来访长途费率批价逻辑及界面展示')),
        verbose_name='子阶段')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '优化局数据流程'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class AuditHistory1(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    stage = models.IntegerField(
        choices=((1, '交流网站问题单收集'), (2, '对应工单查找及附件下载'), (3, '导出系统记录表'), (4, '核对')),
        verbose_name='子阶段')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '补充历史记录(201411至今)'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class AuditHistory2(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    stage = models.IntegerField(
        choices=((1, '交流网站问题单收集'), (2, '对应工单查找及附件下载'), (3, '导出系统记录表'), (4, '核对')),
        verbose_name='子阶段')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '补充历史记录(2011至201410)'
        verbose_name_plural = verbose_name
        ordering = ['itemid']


class AuditProblemStagePercent(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    stage = models.IntegerField(choices=((1, '56个OA文'), (2, '82个OA文'), (3, '协调集团交流网站补发')), verbose_name='子阶段')
    percent = models.IntegerField(verbose_name='占总工作量百分比(单位：%)')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '解决遗留问题各子阶段工作量占比'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class AuditProcedureStagePercent(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    stage = models.IntegerField(choices=((1, '改造交流网站'), (2, '改造工单系统'), (3, '新局数据流程手册更新实施'), (4, '整改国际口来访长途费率批价逻辑及界面展示')), verbose_name='子阶段')
    percent = models.IntegerField(verbose_name='占总工作量百分比(单位：%)')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '优化局数据流程各子阶段工作量占比'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class AuditHistoryStagePercent1(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    stage = models.IntegerField(choices=((1, '交流网站问题单收集'), (2, '对应工单查找及附件下载'), (3, '导出系统记录表'), (4, '核对')), verbose_name='子阶段')
    percent = models.IntegerField(verbose_name='占总工作量百分比(单位：%)')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '补充历史记录(201411至今)各子阶段工作量占比'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class AuditHistoryStagePercent2(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    stage = models.IntegerField(choices=((1, '交流网站问题单收集'), (2, '对应工单查找及附件下载'), (3, '导出系统记录表'), (4, '核对')), verbose_name='子阶段')
    percent = models.IntegerField(verbose_name='占总工作量百分比(单位：%)')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '补充历史记录(2011至201410)各子阶段工作量占比'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class BossOverview(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    stage = models.IntegerField(
        choices=((1, '需求编写'), (2, '验收案例编写'), (3, '验收上线'), (4, '运营流程制定')),
        default=1, verbose_name='阶段')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '国漫流程优化工作总体情况'
        verbose_name_plural = verbose_name
        ordering = ['itemid']


class BossSpec(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    module = models.IntegerField(
        choices=((1, '功能开通'), (2, '产品管理'), (3, '业务办理'), (4, '计费'), (5, '提醒'), (6, '短信管理'), (7, '需求评审'), (8, '根据评审意见修改定版')),
        verbose_name='功能模块')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '国漫优化-需求编写'
        verbose_name_plural = verbose_name
        ordering = ['itemid']


class BossTestCase(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    module = models.IntegerField(
        choices=((1, '功能开通'), (2, '产品管理'), (3, '业务办理'), (4, '计费'), (5, '提醒'), (6, '短信管理'), (7, '整体测试'), (8, '验收案例评审'), (9, '根据评审意见修改定版')),
        verbose_name='功能模块')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '国漫优化-验收案例编写'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class BossAccept(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    module = models.IntegerField(
        choices=((1, '功能开通'), (2, '产品管理'), (3, '业务办理'), (4, '计费'), (5, '提醒'), (6, '短信管理'), (7, '整体测试'), (8, '验收报告出具')),
        verbose_name='功能模块')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '国漫优化-验收测试'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class BossOperationProcess(models.Model):
    itemid = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=500, verbose_name='事宜')
    incharge = models.CharField(max_length=50, verbose_name='负责人')
    plandate = models.DateField(verbose_name='计划完成日期')
    enddate = models.DateField(blank=True, null=True, verbose_name='实际完成日期')
    module = models.IntegerField(
        choices=((1, '功能开通'), (2, '产品管理'), (3, '业务办理'), (4, '计费'), (5, '提醒'), (6, '短信管理'), (7, '运营流程评审'), (8, '根据评审意见修改定版')),
        verbose_name='功能模块')
    state = models.IntegerField(choices=((0,'进行中'),(1,'已完成'),(2,'未启动')), verbose_name='状态')
    note = models.TextField(max_length=20000, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name = '国漫优化-运营流程制定'
        verbose_name_plural = verbose_name
        ordering = ['itemid']

class TodoList(models.Model):
    item = models.TextField(max_length=500)
    intime = models.DateTimeField(default='2016-03-01 0:0:0')
    deletetag = models.IntegerField(default=0)

    class Meta:
        db_table = 'todolist'
        ordering = ['deletetag']