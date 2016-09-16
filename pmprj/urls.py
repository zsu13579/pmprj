"""pmprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pmprj import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pmapp.views.index', name='index'),
    url(r'^meetings/', 'pmapp.views.meetings', name='meetings'),
    url(r'^reports/', 'pmapp.views.reports', name='reports'),
    url(r'^tabledemo/', 'pmapp.views.tabledemo', name='tabledemo'),
    url(r'^auditoverview/', 'pmapp.views.auditoverview', name='auditoverview'),
    url(r'^auditproblem/', 'pmapp.views.auditproblem', name='auditproblem'),
    url(r'^auditprocedure/', 'pmapp.views.auditprocedure', name='auditprocedure'),
    url(r'^audithistory1/', 'pmapp.views.audithistory1', name='audithistory1'),
    url(r'^audithistory2/', 'pmapp.views.audithistory2', name='audithistory2'),
    url(r'^bossoverview/', 'pmapp.views.bossoverview', name='bossoverview'),
    url(r'^bossspecification/', 'pmapp.views.bossspecification', name='bossspecification'),
    url(r'^bosstestcase/', 'pmapp.views.bosstestcase', name='bosstestcase'),
    url(r'^bossaccept/', 'pmapp.views.bossaccept', name='bossaccept'),
    url(r'^bossoperationprocess/', 'pmapp.views.bossoperationprocess', name='bossoperationprocess'),
    url(r'^dashboard/', 'pmapp.views.dashboard', name='dashboard'),
    url(r'^todolist/', 'pmapp.views.todolist', name='todolist'),
    url(r'^dosearch/', 'pmapp.views.dosearch'),
    url(r'^additem/', 'pmapp.views.additem'),
    url(r'^saveedit/', 'pmapp.views.saveedit'),
    url(r'^delete_ajax/', 'pmapp.views.delete_ajax'),
    url(r"^uploads/(?P<path>.*)$", \
        "django.views.static.serve", \
        {"document_root": settings.MEDIA_ROOT, }),
    url(r"^download/(?P<path>.*)$", \
        "django.views.static.serve", \
        {"document_root": settings.MEDIA_ROOT+'/report', }),
]
