# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField
from django.template.defaultfilters import default

def generate_filename(self, filename):
    url = '/'.join(['content',self.title, filename])
    return url

def nu():
        no = Regulation.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
def nu2():
        no = Handbook.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
def nu3():
        no = Notice.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

class Code(models.Model):
    codeid = models.IntegerField(default=1)
    codename = models.CharField(('코드이름'),max_length=50)
    where = models.CharField(('코드분류'),max_length=50)
    codenumber = models.IntegerField(('코드 구분 번호'),default=1)
    def __unicode__(self):
        return self.codename
        
class Notice(models.Model):
    num = models.IntegerField(default=nu3)
    title = models.CharField(('제목'),max_length=200)
    content = RichTextField(('내용'))
    uploadfile = models.FileField(('첨부파일'),upload_to=generate_filename,null=True,blank=True)
    writer = models.CharField(('작성자'),max_length=200)
    date = models.DateField()
    code = models.ForeignKey(Code,null=True)
    def __unicode__(self):
        return self.title

class Handbook(models.Model):
    num = models.IntegerField(default=nu2)
    title = models.CharField(('제목'),max_length=200)
    document = models.FileField(('자료'),upload_to=generate_filename,null=True,blank=True)
    writer = models.CharField(('작성자'),max_length=200)
    code = models.ForeignKey(Code,null=True)
    def __unicode__(self):
        return self.title
    
class Regulation(models.Model):
    
    num = models.IntegerField(default=nu)
    title = models.CharField(('제목'), max_length=200)
    document = models.FileField(('자료'),upload_to=generate_filename,null=True,blank=True)
    writer = models.CharField(('작성자'),max_length=200)
    code = models.ForeignKey(Code,null=True)
    def __unicode__(self):
        return self.title

class Commission(models.Model):
    num = models.IntegerField(default=1)
    title = models.CharField(('제목'),max_length=200)
    content = RichTextField(('내용'))
    uploadfile = models.FileField(('첨부파일'),upload_to=generate_filename,null=True,blank=True)
    writer = models.CharField(('작성자'),max_length=200)
    date = models.DateField()
    code = models.ForeignKey(Code,null=True)
    def __unicode__(self):
        return self.title

class Graph(models.Model):
    title = models.CharField(max_length=200)
    