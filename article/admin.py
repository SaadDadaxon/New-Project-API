from django.contrib import admin
from .models import Article, Tag, Category, SubContent, SubContentImage, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_date']
    list_filter = ['category', 'tags']
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags',)
    search_fields = ['title']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class SubconAdmin(admin.ModelAdmin):
    list_display = ['id', 'article']


class SubConImgAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcontent', 'image', 'is_wide']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'article', 'created_date']
    date_hierarchy = 'created_date'
    search_fields = ['author__username', 'article__title', 'author__first_name', 'author__last_name']
    autocomplete_fields = ['author', 'article']


admin.site.register(Article, ArticleAdmin),
admin.site.register(Tag, TagAdmin),
admin.site.register(Category, CategoryAdmin),
admin.site.register(SubContent, SubconAdmin),
admin.site.register(SubContentImage, SubConImgAdmin),
admin.site.register(Comment, CommentAdmin),



