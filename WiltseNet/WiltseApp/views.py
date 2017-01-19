# -*- coding: utf-8 -*-
from django.shortcuts import render
from WiltseApp.models import *
from django.shortcuts import (render,get_object_or_404,redirect)
from django.forms.formsets import formset_factory
from django.http import Http404
#from django.db.models.Field import Empty
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Create your views here.
def mainpage(request):
    list = Notice.objects.filter()
    return render(request,'index.html',{'list':list})

@csrf_exempt
def contview(request):
    import json
    getnum = request.POST['num']
    output = Notice.objects.filter(num=getnum)
    data = serializers.serialize('json', output)
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data)
    '''
    getnum = request.POST['num']
    output = Notice.objects.filter(num=getnum)
    return HttpResponse(output,content_type = "application/json")
    '''
def doculist(request,category_id):
    list = Handbook.objects.filter(code__codenumber=category_id)
    return render(request, 'documents/document.html', {'list':list})

@csrf_exempt
def docuview(request):
    import json
    getnum = request.POST['num']
    output = Handbook.objects.filter(num=getnum)
    data = serializers.serialize('json', output)
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data)