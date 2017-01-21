# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 10:42
from __future__ import unicode_literals

import WiltseApp.models
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WiltseApp', '0011_auto_20170118_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=200, verbose_name='\uc81c\ubaa9')),
                ('content', ckeditor.fields.RichTextField(verbose_name='\ub0b4\uc6a9')),
                ('uploadfile', models.FileField(blank=True, null=True, upload_to=WiltseApp.models.generate_filename, verbose_name='\ucca8\ubd80\ud30c\uc77c')),
                ('writer', models.CharField(max_length=200, verbose_name='\uc791\uc131\uc790')),
                ('date', models.DateField()),
                ('code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WiltseApp.Code')),
            ],
        ),
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=200, verbose_name='\uc81c\ubaa9')),
                ('document', models.FileField(blank=True, null=True, upload_to=WiltseApp.models.generate_filename, verbose_name='\uc790\ub8cc')),
                ('writer', models.CharField(max_length=200, verbose_name='\uc791\uc131\uc790')),
                ('code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WiltseApp.Code')),
            ],
        ),
        migrations.AlterField(
            model_name='handbook',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=WiltseApp.models.generate_filename, verbose_name='\uc790\ub8cc'),
        ),
    ]
