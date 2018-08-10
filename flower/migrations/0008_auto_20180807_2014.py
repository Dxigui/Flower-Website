# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-07 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0007_auto_20180807_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusmodel',
            name='btTag',
            field=models.ForeignKey(help_text='与网页底部导航栏关联，可以在底部导航栏跳转到关于我们的页面', on_delete=django.db.models.deletion.CASCADE, to='flower.BootTag', verbose_name='关联的底部导航栏'),
        ),
    ]
