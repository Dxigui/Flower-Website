# -*- coding: utf-8 -*-

import markdown
from django.shortcuts import render, HttpResponseRedirect, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import AboutUsModel, Product, Terminal, Carousel, BackgroundImage


def logo(request):
    """

    :param request:
    :return:
    """

    return render(request, 'flower/index.html')

def index(request):
    """
        首页视图
    """
    carousels_list = Carousel.objects.all().order_by('-number')[:3]
    new_products_list = Product.objects.all().order_by('-create_time')[:6]
    background_image = BackgroundImage.objects.all().order_by('-create_time')[0]
    boot_nav_list = AboutUsModel.objects.all()
    context = {
        'carousels_list': carousels_list,
        'new_products_list': new_products_list,
        'boot_nav_list': boot_nav_list,
        'background_image': background_image
    }
    return render(request, 'flower/index.html', context)


class ProductView(ListView):
    """
    继承 ListView 通用视图
    """
    model = Product
    template_name = 'flower/products.html'
    context_object_name = 'products_list'
    paginate_by = 9




class TerminalView(ListView):
    model = Terminal
    template_name = 'flower/terminal.html'
    context_object_name = 'terminals_list'
    paginate_by = 6



def AboutUs(request, pk):
    """
     关于我们的视图
    :param request:
    :return:
    """
    get_brand = get_object_or_404(AboutUsModel, pk=pk)
    get_brand_list = AboutUsModel.objects.all().order_by('id')
    get_brand.body = markdown.markdown(get_brand.body,
                                       extensions=[
                                           'markdown.extensions.extra',
                                           'markdown.extensions.codehilite'
                                       ]
                                       )
    context = {
        'get_brand': get_brand,
        'get_brand_list': get_brand_list
    }
    return render(request, 'flower/aboutus.html', context)
