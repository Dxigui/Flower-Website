from django import template

from ..models import AboutUsModel, BootTag, Terminal, KeyWords

register = template.Library()

@register.simple_tag
def get_about_us_nav_list():
    return AboutUsModel.objects.all().order_by('id')[0]

@register.simple_tag
def get_boot_tag_list():
    return BootTag.objects.all()

@register.simple_tag
def brand_to_str():
    brands = AboutUsModel.objects.all()
    return ','.join([brand.title for brand in brands])

@register.simple_tag
def terminal_title():
    terminal_pic = Terminal.objects.all()[:6]
    return ','.join([t.title for t in terminal_pic])

@register.simple_tag
def get_keyword():
    keywords = KeyWords.objects.all()
    return ','.join([k.keywd for k in keywords])