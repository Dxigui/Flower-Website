# -*- coding: utf-8 -*-
import markdown
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.html import strip_tags

# 文章关键字
class ArticleKeyWords(models.Model):
    name = models.CharField(max_length=20, verbose_name='文章关键字',
                            help_text='SEO 优化')

    class Meta:
        verbose_name = '文章关键字'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='文章标题')
    body = models.TextField(verbose_name='文章主体内容，用Markdown编写')
    create_time = models.DateTimeField(verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间',
                                       help_text='修改时间可以为空')
    likes = models.IntegerField(default=0, verbose_name='点赞')
    views = models.IntegerField(default=0, verbose_name='阅读数')
    excerpt = models.CharField(max_length=240, blank=True, verbose_name='摘要',
                               help_text='内容摘要，240字内，如果不填写则默认取前240个字')
    user = models.ForeignKey(User, verbose_name='文章作者')
    articlekeywd = models.ManyToManyField(ArticleKeyWords, verbose_name='关联文章关键字',
                                          help_text='选择一个或多个文章关键字')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite'
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:240]
        super(Article, self).save(*args, **kwargs)

# 评论
class Comment(models.Model):
    name = models.CharField(max_length=30, verbose_name='用户名')
    text = models.TextField(verbose_name='内容')
    create_date = models.DateTimeField(verbose_name='时间')
    Article = models.ForeignKey(Article, verbose_name='评论的文章')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.name