# -*- coding: utf-8 -*-

from django.contrib import admin

from flower.models import AboutUsModel, KeyWords, Category, Product, Carousel, Terminal, BootTag

class AboutUsModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'btTag')
    # list_filter = ('b?tTag',)
    list_per_page = 10
    search_fields = ('title', 'id', 'btTag')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_per_page = 10
    search_fields = ('name', 'id')

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'number', 'img_url')
    list_per_page = 10
    search_fields = ('title', 'number', 'id')

class ProductAmin(admin.ModelAdmin):
    list_display = ('flower_name', 'id', 'price', 'create_time',
                    'img_link', 'category')
    list_filter = ('create_time',)
    list_per_page = 10
    search_fields = ('flower_name', 'price', 'category', 'keywords', 'id')
    filter_horizontal = ('keywords',)

class TerminalAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'description', 'create_time', 'img_link')
    list_filter = ('create_time',)
    list_per_page = 10
    search_fields = ('title', 'id')

class KeyWordsAdmin(admin.ModelAdmin):
    list_display = ('keywd', 'id')
    list_per_page = 10
    search_fields = (
        'keywd',
        'id'
    )

class BootTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    list_per_page = 10
    search_fields = ('title', 'id')



admin.site.register(AboutUsModel, AboutUsModelAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Product, ProductAmin)
admin.site.register(Terminal, TerminalAdmin)
admin.site.register(KeyWords, KeyWordsAdmin)
admin.site.register(BootTag, BootTagAdmin)
