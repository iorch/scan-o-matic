#!/usr/bin/env python
# coding=utf-8

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def the_site(request):
    now = datetime.datetime.now()
    t = get_template('index.html')
    html = t.render(Context({}))
    return HttpResponse(html)
