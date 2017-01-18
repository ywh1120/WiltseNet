# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-17 10:43
from __future__ import unicode_literals

import WiltseApp.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codenum', models.IntegerField()),
                ('codename', models.CharField(max_length=50)),
                ('where', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('title', models.CharField(max_length=200, verbose_name='\uc81c\ubaa9')),
                ('content', ckeditor.fields.RichTextField(verbose_name='\ub0b4\uc6a9')),
                ('uploadfile', models.FileField(null='true', upload_to=WiltseApp.models.generate_filename, verbose_name='\ucca8\ubd80\ud30c\uc77c')),
                ('writer', models.CharField(max_length=200, verbose_name='\uc791\uc131\uc790')),
                ('date', models.DateField()),
            ],
        ),
    ]
