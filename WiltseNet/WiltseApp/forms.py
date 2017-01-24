# -*- coding: utf-8 -*-

from django import forms
from WiltseApp.models import *
from django.contrib.auth.models import User
from ckeditor.widgets import *

class NotiFrom(forms.models):
    title = forms.CharField(required=True)
    content = forms.CharField(widget=CKEditorWidget())
    uploadfile = forms.FileField()
    writer = forms.CharField(required=True)
    #code = forms.se