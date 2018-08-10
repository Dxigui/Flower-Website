# -*- coding: utf-8 -*-
import time

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse
import datetime
import markdown

from .models import Article, Comment


class OurStoryView(ListView):
    """
    通过类封装视图函数
    继承 Django 内置 ListView 通用类，实现文章展示视图
    """
    model = Article
    template_name = 'blog/ourstory.html'
    context_object_name = 'articles_list'
    # 开启分页功能，每页 8 篇文章
    paginate_by = 8




def detail(request, pk):
    """
    文章详情页
    :param request:
    :return:
    """
    get_article = get_list_or_404(Article, pk=pk)
    get_article_info = get_object_or_404(Article, pk=pk)
    get_article_info.body = markdown.markdown(get_article_info.body,
                                              extensions =[
                                                  'markdown.extensions.extra',
                                                  'markdown.extensions.codehilite'
                                              ]
                                              )
    # 给阅读数量增加一个限定，至少五分钟才能增加一次阅读量
    ses = request.session
    the_key = 'is_read_{}'.format(get_article_info.id)
    is_read_time = ses.get(the_key)
    if not is_read_time:
        get_article_info.increase_views()
        ses[the_key] = time.time()
    else:
        now_time = time.time()
        t = now_time - is_read_time
        if t > 60 * 5:
            get_article_info.increase_views()
            ses[the_key] = time.time()
    if request.method == 'GET':
        context = {
            'get_article': get_article,
            'get_article_info': get_article_info
        }
        return render(request, 'blog/detail.html', context)

def archives(request, year, month):
    """
    归档视图，按年月进行归档
    :param request:
    :param year:
    :param month:
    :return:
    """
    get_archive_articles = Article.objects.filter(
        create_time__year=year,
        create_time__month=month
    ).order_by('-create_time')
    context = {
        'get_archive_articles': get_archive_articles
    }
    return render(request, 'blog/archives.html', context)
