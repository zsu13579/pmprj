#-*- coding: utf-8 -*-
from django.contrib import admin
from pmapp.models import *

# Register your models here.

class WorkitemAdmin(admin.ModelAdmin):
  # fields = ('title','desc','content',)
  list_display = ('itemid', 'name', 'category', 'progress','plan','state',)
  list_display_links = ('itemid', 'name',)
  # list_editable = ('itemid','name', 'category', 'progress','plan','state',)

admin.site.register(Workitem, WorkitemAdmin)

class MeetingAdmin(admin.ModelAdmin):
  # fields = ('title','desc','content',)
  list_display = ('meetingid', 'date', 'memo', 'attender','type',)
  list_display_links = ('meetingid', 'date', 'memo')
  # list_editable = ('itemid','name', 'category', 'progress','plan','state',)

admin.site.register(Meeting, MeetingAdmin)

class ReportAdmin(admin.ModelAdmin):
  # fields = ('title','desc','content',)
  list_display = ('reportid', 'dateperiod', 'date', 'content',)
  list_display_links = ('reportid', 'dateperiod', 'date', 'content')
  # list_editable = ('itemid','name', 'category', 'progress','plan','state',)
  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(Report, ReportAdmin)

class AuditOverviewAdmin(admin.ModelAdmin):
  list_display = ('itemid', 'stage', 'incharge', 'plandate', 'enddate',  'state', 'note',)
  list_display_links = ('itemid', 'stage')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(AuditOverview, AuditOverviewAdmin)

class AuditProblemAdmin(admin.ModelAdmin):
  list_display = ('itemid', 'name', 'incharge', 'plandate', 'enddate',  'stage', 'state', 'note',)
  list_display_links = ('itemid', 'name')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(AuditProblem, AuditProblemAdmin)

class AuditProcedureAdmin(admin.ModelAdmin):
  list_display = ('itemid', 'name', 'incharge', 'plandate', 'enddate',  'stage', 'state', 'note',)
  list_display_links = ('itemid', 'name')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(AuditProcedure, AuditProcedureAdmin)

class Audithistory1Admin(admin.ModelAdmin):
  list_display = ('itemid', 'name', 'incharge', 'plandate', 'enddate',  'stage', 'state', 'note',)
  list_display_links = ('itemid', 'name')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(AuditHistory1, Audithistory1Admin)

class Audithistory2Admin(admin.ModelAdmin):
  list_display = ('itemid', 'name', 'incharge', 'plandate', 'enddate',  'stage', 'state', 'note',)
  list_display_links = ('itemid', 'name')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(AuditHistory2, Audithistory2Admin)


class BossOverviewAdmin(admin.ModelAdmin):
  list_display = ('itemid', 'stage', 'incharge', 'plandate', 'enddate',  'state', 'note',)
  list_display_links = ('itemid', 'stage')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(BossOverview, BossOverviewAdmin)


class BossSpecAdmin(admin.ModelAdmin):
  list_display = ('itemid', 'name', 'incharge', 'plandate', 'enddate',  'module', 'state', 'note',)
  list_display_links = ('itemid', 'name')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(BossSpec, BossSpecAdmin)

class BossTestcaseAdmin(admin.ModelAdmin):
  list_display = ('itemid', 'name', 'incharge', 'plandate', 'enddate',  'module', 'state', 'note',)
  list_display_links = ('itemid', 'name')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(BossTestCase, BossTestcaseAdmin)

class BossAcceptAdmin(admin.ModelAdmin):
  list_display = ('itemid', 'name', 'incharge', 'plandate', 'enddate',  'module', 'state', 'note',)
  list_display_links = ('itemid', 'name')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(BossAccept, BossAcceptAdmin)

class BossOperationProcessAdmin(admin.ModelAdmin):
  list_display = ('itemid', 'name', 'incharge', 'plandate', 'enddate',  'module', 'state', 'note',)
  list_display_links = ('itemid', 'name')

  class Media:
    js = (
      '/static/js/kindeditor/kindeditor-all-min.js',
      '/static/js/kindeditor/lang/zh_CN.js',
      '/static/js/kindeditor/config.js',
    )

admin.site.register(BossOperationProcess, BossOperationProcessAdmin)