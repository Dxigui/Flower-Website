from django.contrib import admin
from .models import Article, Comment, ArticleKeyWords

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'excerpt', 'create_time',
                    'modify_time', 'likes', 'views', 'user')
    list_filter = ('create_time',)
    # list_editable = ('title', 'body')
    list_per_page = 10
    search_fields = ('title', 'id')
    raw_id_fields = ('user',)
    filter_horizontal = ('articlekeywd',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'text', 'create_date')
    list_per_page = 10
    search_fields = ('name', 'id')

class ArticlleKeyWordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_per_page = 10
    search_fields = ('name', 'id')

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleKeyWords, ArticlleKeyWordsAdmin)
# admin.site.register(Comment, CommentAdmin)
