# -*- coding: utf-8 -*-
from django.shortcuts import render
from WiltseApp.models import *
from django.shortcuts import (render,get_object_or_404,redirect)
from django.forms.formsets import formset_factory
from django.http import Http404
#from django.db.models.Field import Empty
from django.forms.models import modelformset_factory
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from datetime import datetime
#from WiltseNet.WiltseApp.models import Notice
# Create your views here.
def mainpage(request):
    list = Notice.objects.filter()
    cate = Code.objects.filter(where="공지사항")
    return render(request,'index.html',{'list':list,'category':cate})

@csrf_exempt
def login_ajax(request):
    username= request.POST['username']
    password = request.POST['pwd']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            list = Notice.objects.filter()
            cate = Code.objects.filter(where="공지사항")
            return render(request,'index.html',{'list':list,'category':cate})
        else:
            return HttpResponse('관리자에게 문의 하시기 바랍니다.')
    else:
        return HttpResponse('아이디 또는 비밀번호를 확인하세요.')

@csrf_exempt
def notice_write(request):
    if request.method == 'POST':
        titlebox = request.POST['titlebox']
        writecontent = request.POST['writecontent']
        uploadfile1 = request.POST['uploadfile']
        cate = request.POST['cate']
        
        new_notice = Notice(title = titlebox,content = writecontent,uploadfile = uploadfile1,date = datetime.now(),code = Code.objects.get(codenumber=cate))
        new_notice.save()    
    
    list = Notice.objects.filter()
    cate = Code.objects.filter(where="공지사항")
    return render(request,'index.html',{'list':list,'category':cate})

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

def docu2list(request,category_id):
    list = Regulation.objects.filter(code__codenumber=category_id)
    return render(request, 'documents/document2.html', {'list':list})

@csrf_exempt
def docuview(request):
    import json
    getnum = request.POST['num']
    output = Handbook.objects.filter(num=getnum)
    data = serializers.serialize('json', output)
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data)

@csrf_exempt
def docu2view(request):
    import json
    getnum = request.POST['num']
    output = Regulation.objects.filter(num=getnum)
    data = serializers.serialize('json', output)
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data)