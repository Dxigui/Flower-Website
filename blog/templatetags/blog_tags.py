# -*- coding: utf-8 -*-
from django import template
from ..models import Article, ArticleKeyWords


register = template.Library()

@register.simple_tag
def archives():
    num = 5
    return Article.objects.dates('create_time', 'month', order='DESC')[:num]

@register.simple_tag
def article_to_str(art):
    # article = Article.objects.filter(id)
    # for ar in art:
    keywds = art.articlekeywd.all()
    return ','.join([key.name for key in keywds])