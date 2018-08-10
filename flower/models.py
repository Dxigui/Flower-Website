import markdown
from django.db import models
from django.shortcuts import reverse

# 产品关键词
class KeyWords(models.Model):
    keywd = models.CharField(max_length=20, verbose_name='关键词',
                             help_text='产品关键词，提供 SEO 优化')

    class Meta:
        verbose_name = '产品关键词'
        verbose_name_plural = verbose_name
        ordering = ['keywd']

    def __str__(self):
        return self.keywd

# 滚动图片
class Carousel(models.Model):
    number = models.IntegerField(unique=True, verbose_name='编号', help_text='编号决定图片播放顺序,少于三个')
    title = models.CharField(max_length=20, blank=True, null=True, verbose_name='标题',
                             help_text='标题可以为空')
    img_url = models.CharField(max_length=255, verbose_name='图片地址')

    class Meta:
        verbose_name = '图片轮播'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.title

# 背景图
class BackgroundImage(models.Model):
    img_link = models.CharField(max_length=255, verbose_name='背景图')
    create_time = models.DateTimeField(verbose_name='创建时间',
                                       help_text='显示最新创建的图片')

    class Meta:
        verbose_name = '首页关于我们简介背景图'
        verbose_name_plural = verbose_name

# 底部导航栏
class BootTag(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')

    class Meta:
        verbose_name = '底部导航栏标题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 关于我们
class AboutUsModel(models.Model):
    title = models.CharField(max_length=64, verbose_name='侧边导航栏')
    body = models.TextField(verbose_name='内容',
                            help_text='支持 Markdown 语法')

    btTag = models.ForeignKey(BootTag, verbose_name='关联的底部导航栏',
                              help_text='与网页底部导航栏关联，可以在底部导航栏跳转到关于我们的页面')

    class Meta:
        verbose_name = '关于我们'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 产品分类
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='类名')

    class Meta:
        verbose_name = '产品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_product_list(self):
        return Product.objects.filter(category=self)

# 产品
class Product(models.Model):
    IMG_LINK = 'flower/images/flower-1.jpg'
    flower_name = models.CharField(max_length=64, verbose_name='花名')
    detail = models.TextField(max_length=150, verbose_name='简要描述',help_text='150字以内的产品描述')
    price = models.FloatField(verbose_name='价格')
    img_link = models.CharField(max_length=255, default=IMG_LINK, verbose_name='图片地址')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='产品分类')
    keywords = models.ManyToManyField(KeyWords, verbose_name='关键词',
                                      help_text='关键词用来作为SEO中的keywords，数量为3-4个')

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.flower_name

    def body_to_markdown(self):
        return markdown.Markdown(self.detail, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

# 终端形象
class Terminal(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    description = models.CharField(max_length=20, blank=True, null=True, verbose_name='描述',
                                   help_text='20字以内的描述')
    img_link = models.CharField(max_length=255, verbose_name='图片地址')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '终端形象（图片）'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title