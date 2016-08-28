#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from pmapp.models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from datetime import datetime
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    workitems1 = Workitem.objects.filter(category="新产品支撑工作")
    workitems2 = Workitem.objects.filter(category="经分支撑工作")
    return render(request, 'index.html', locals())

def meetings(request):
    count = Meeting.objects.all().count
    countmts = Meeting.objects.all().__len__()
    countpage = countmts / 2
    meetings = getpage(request,Meeting.objects.all())
    return render(request, 'meetings.html', locals())

def reports(request):
    try:
        reportid = request.GET.get("reportid")
        report = Report.objects.get(reportid=reportid)
    except:
        report = Report.objects.all()[0]
    report_list = Report.objects.all()
    return render(request, 'reports.html', locals())

def auditoverview(request):
    audit_overview_list = AuditOverview.objects.all()

    count1done = AuditProblem.objects.filter(state=1).count
    count1all = AuditProblem.objects.all().count

    count2done = AuditProcedure.objects.filter(state=1).count
    count2all = AuditProcedure.objects.all().count

    count3done = AuditHistory1.objects.filter(state=1).count
    count3all = AuditHistory1.objects.all().count

    count4done = AuditHistory2.objects.filter(state=1).count
    count4all = AuditHistory2.objects.all().count

    return render(request, 'auditoverview.html', locals())

def auditproblem(request):
    audit_problem_list1 = AuditProblem.objects.filter(stage=1)
    audit_problem_list2 = AuditProblem.objects.filter(stage=2)
    audit_problem_list3 = AuditProblem.objects.filter(stage=3)
    audit_problem_list4 = AuditProblem.objects.filter(stage=4)

    count1done = AuditProblem.objects.filter(stage=1, state=1).count
    count1all = audit_problem_list1.count

    count2done = AuditProblem.objects.filter(stage=2, state=1).count
    count2all = audit_problem_list2.count

    count3done = AuditProblem.objects.filter(stage=3, state=1).count
    count3all = audit_problem_list3.count

    count4done = AuditProblem.objects.filter(stage=4, state=1).count
    count4all = audit_problem_list4.count


    return render(request, 'auditproblem.html', locals())

def auditprocedure(request):
    audit_procedure_list1 = AuditProcedure.objects.filter(stage=1)
    audit_procedure_list2 = AuditProcedure.objects.filter(stage=2)
    audit_procedure_list3 = AuditProcedure.objects.filter(stage=3)
    audit_procedure_list4 = AuditProcedure.objects.filter(stage=4)

    count1done = AuditProcedure.objects.filter(stage=1, state=1).count
    count1all = audit_procedure_list1.count

    count2done = AuditProcedure.objects.filter(stage=2, state=1).count
    count2all = audit_procedure_list2.count

    count3done = AuditProcedure.objects.filter(stage=3, state=1).count
    count3all = audit_procedure_list3.count

    count4done = AuditProcedure.objects.filter(stage=4, state=1).count
    count4all = audit_procedure_list4.count

    return render(request, 'auditprocedure.html', locals())

def audithistory1(request):

    audit_stage1_list1 = AuditHistory1.objects.filter(stage=1)
    audit_stage1_list2 = AuditHistory1.objects.filter(stage=2)
    audit_stage1_list3 = AuditHistory1.objects.filter(stage=3)
    audit_stage1_list4 = AuditHistory1.objects.filter(stage=4)

    count1done = AuditHistory1.objects.filter(stage=1, state=1).count
    count1all = audit_stage1_list1.count

    count2done = AuditHistory1.objects.filter(stage=2, state=1).count
    count2all = audit_stage1_list2.count

    count3done = AuditHistory1.objects.filter(stage=3, state=1).count
    count3all = audit_stage1_list3.count

    count4done = AuditHistory1.objects.filter(stage=4, state=1).count
    count4all = audit_stage1_list4.count

    return render(request, 'audithistory1.html', locals())

def audithistory2(request):

    audit_stage1_list1 = AuditHistory2.objects.filter(stage=1)
    audit_stage1_list2 = AuditHistory2.objects.filter(stage=2)
    audit_stage1_list3 = AuditHistory2.objects.filter(stage=3)
    audit_stage1_list4 = AuditHistory2.objects.filter(stage=4)

    count1done = AuditHistory2.objects.filter(stage=1, state=1).count
    count1all = audit_stage1_list1.count

    count2done = AuditHistory2.objects.filter(stage=2, state=1).count
    count2all = audit_stage1_list2.count

    count3done = AuditHistory2.objects.filter(stage=3, state=1).count
    count3all = audit_stage1_list3.count

    count4done = AuditHistory2.objects.filter(stage=4, state=1).count
    count4all = audit_stage1_list4.count

    return render(request, 'audithistory2.html', locals())

def bossoverview(request):

    boss_overview_list = BossOverview.objects.all()

    count1done = BossSpec.objects.filter(state=1).count
    count1all = BossSpec.objects.all().count

    count2done = BossTestCase.objects.filter(state=1).count
    count2all = BossTestCase.objects.all().count

    count3done = BossAccept.objects.filter(state=1).count
    count3all = BossAccept.objects.all().count

    count4done = BossOperationProcess.objects.filter(state=1).count
    count4all = BossOperationProcess.objects.all().count

    return render(request, 'bossoverview.html', locals())

def bossspecification(request):

    boss_spec_list1 = BossSpec.objects.filter(module=1)
    boss_spec_list2 = BossSpec.objects.filter(module=2)
    boss_spec_list3 = BossSpec.objects.filter(module=3)
    boss_spec_list4 = BossSpec.objects.filter(module=4)
    boss_spec_list5 = BossSpec.objects.filter(module=5)
    boss_spec_list6 = BossSpec.objects.filter(module=6)
    boss_spec_list7 = BossSpec.objects.filter(module=7)
    boss_spec_list8 = BossSpec.objects.filter(module=8)

    count1done = BossSpec.objects.filter(module=1, state=1).count() + BossSpec.objects.filter(module=2, state=1).count() + BossSpec.objects.filter(module=3, state=1).count()
    count1all = boss_spec_list1.count() + boss_spec_list2.count() + boss_spec_list3.count()

    count2done = BossSpec.objects.filter(module=4, state=1).count
    count2all = boss_spec_list4.count

    count3done = BossSpec.objects.filter(module=5, state=1).count() + BossSpec.objects.filter(module=6, state=1).count()
    count3all = boss_spec_list5.count() + boss_spec_list6.count()

    count4done = BossSpec.objects.filter(module=7, state=1).count() + BossSpec.objects.filter(module=8, state=1).count()
    count4all = boss_spec_list7.count() + boss_spec_list8.count()

    return render(request, 'bossspecification.html', locals())

def bosstestcase(request):

    boss_testcase_list1 = BossTestCase.objects.filter(module=1)
    boss_testcase_list2 = BossTestCase.objects.filter(module=2)
    boss_testcase_list3 = BossTestCase.objects.filter(module=3)
    boss_testcase_list4 = BossTestCase.objects.filter(module=4)
    boss_testcase_list5 = BossTestCase.objects.filter(module=5)
    boss_testcase_list6 = BossTestCase.objects.filter(module=6)
    boss_testcase_list7 = BossTestCase.objects.filter(module=7)
    boss_testcase_list8 = BossTestCase.objects.filter(module=8)
    boss_testcase_list9 = BossTestCase.objects.filter(module=9)

    count1done = BossTestCase.objects.filter(module=1, state=1).count() + BossTestCase.objects.filter(module=2, state=1).count() + BossTestCase.objects.filter(module=3, state=1).count()
    count1all = boss_testcase_list1.count() + boss_testcase_list2.count() + boss_testcase_list3.count()

    count2done = BossTestCase.objects.filter(module=4, state=1).count
    count2all = boss_testcase_list4.count

    count3done = BossTestCase.objects.filter(module=5, state=1).count() + BossTestCase.objects.filter(module=6, state=1).count() + BossTestCase.objects.filter(module=7, state=1).count()
    count3all = boss_testcase_list5.count() + boss_testcase_list6.count() + boss_testcase_list7.count()

    count4done = BossTestCase.objects.filter(module=8, state=1).count() + BossTestCase.objects.filter(module=9, state=1).count()
    count4all = boss_testcase_list8.count() + boss_testcase_list9.count()

    return render(request, 'bosstestcase.html', locals())

def bossaccept(request):
    boss_accept_list1 = BossAccept.objects.filter(module=1)
    boss_accept_list2 = BossAccept.objects.filter(module=2)
    boss_accept_list3 = BossAccept.objects.filter(module=3)
    boss_accept_list4 = BossAccept.objects.filter(module=4)
    boss_accept_list5 = BossAccept.objects.filter(module=5)
    boss_accept_list6 = BossAccept.objects.filter(module=6)
    boss_accept_list7 = BossAccept.objects.filter(module=7)
    boss_accept_list8 = BossAccept.objects.filter(module=8)

    count1done = BossAccept.objects.filter(module=1, state=1).count() + BossAccept.objects.filter(module=2,state=1).count() + BossAccept.objects.filter(module=3, state=1).count()
    count1all = boss_accept_list1.count() + boss_accept_list2.count() + boss_accept_list3.count()

    count2done = BossAccept.objects.filter(module=4, state=1).count
    count2all = boss_accept_list4.count

    count3done = BossAccept.objects.filter(module=5, state=1).count() + BossAccept.objects.filter(module=6,state=1).count()
    count3all = boss_accept_list5.count() + boss_accept_list6.count()

    count4done = BossAccept.objects.filter(module=7, state=1).count() + BossAccept.objects.filter(module=8, state=1).count()
    count4all = boss_accept_list7.count() + boss_accept_list8.count()

    return render(request, 'bossaccept.html', locals())

def bossoperationprocess(request):

    boss_operation_list1 = BossOperationProcess.objects.filter(module=1)
    boss_operation_list2 = BossOperationProcess.objects.filter(module=2)
    boss_operation_list3 = BossOperationProcess.objects.filter(module=3)
    boss_operation_list4 = BossOperationProcess.objects.filter(module=4)
    boss_operation_list5 = BossOperationProcess.objects.filter(module=5)
    boss_operation_list6 = BossOperationProcess.objects.filter(module=6)
    boss_operation_list7 = BossOperationProcess.objects.filter(module=7)
    boss_operation_list8 = BossOperationProcess.objects.filter(module=8)

    count1done = BossOperationProcess.objects.filter(module=1, state=1).count() + BossOperationProcess.objects.filter(module=2, state=1).count() + BossOperationProcess.objects.filter(module=3, state=1).count()
    count1all = boss_operation_list1.count() + boss_operation_list2.count() + boss_operation_list3.count()

    count2done = BossOperationProcess.objects.filter(module=4, state=1).count
    count2all = boss_operation_list4.count

    count3done = BossOperationProcess.objects.filter(module=5, state=1).count() + BossOperationProcess.objects.filter(module=6, state=1).count()
    count3all = boss_operation_list5.count() + boss_operation_list6.count()

    count4done = BossOperationProcess.objects.filter(module=7, state=1).count() + BossOperationProcess.objects.filter(module=8, state=1).count()
    count4all = boss_operation_list7.count() + boss_operation_list8.count()

    return render(request, 'bossoperationprocess.html', locals())

def dashboard(request):
    pass
    return render(request, 'dashboard.html', locals())

# todolist view begin


def todolist(request):
    todolist = TodoList.objects.all()
    paginator = Paginator(todolist, 3)
    page = request.GET.get('page')
    try:
        tl = paginator.page(page)
    except PageNotAnInteger:
        tl = paginator.page(1)
    except EmptyPage:
        tl = paginator.page(paginator.num_pages)
    return render(request,'todolist.html',locals())

def dosearch(request):
    try:
        item = request.GET.get("searchitem")
    except:
        pass
    if(item):
        todolist = TodoList.objects.filter(item__contains=item)
    else:
        todolist = TodoList.objects.all()
    paginator = Paginator(todolist,3)
    page = request.GET.get('page')
    try:
        tl = paginator.page(page)
    except PageNotAnInteger:
        tl = paginator.page(1)
    except EmptyPage:
        tl = paginator.page(paginator.num_pages)

    return render(request, 'todolist.html', locals())

def additem(request):

    try:
        item = request.GET.get('item')
        newitem = TodoList(item=item,intime=datetime.now())
        newitem.save()
    except Exception as e:
        raise e

    return redirect(request.META['HTTP_REFERER'])

def saveedit(request):

    try:
        edititem = request.GET.get('edititem')
        id = request.GET.get('id')
        updateitem = TodoList.objects.get(id=id)
        updateitem.item=edititem
        updateitem.intime=datetime.now()
        updateitem.save()
    except Exception as e:
        raise e

    return redirect(request.META['HTTP_REFERER'])

def delete_ajax(request):

    try:
        item = request.GET.get('item')
        delteitem = TodoList.objects.get(item=item)
        delteitem.deletetag=1
        delteitem.save()
    except Exception as e:
        raise e

    return HttpResponse(json.dumps({"result":1}), content_type="application/json")

# todolist view end

def getpage(request,meetings):
    try:
        paginator = Paginator(meetings, 2)
        page = request.GET.get('page')
        meetings = paginator.page(page)

    except (EmptyPage, InvalidPage, PageNotAnInteger):
        meetings = paginator.page(1)
    return meetings