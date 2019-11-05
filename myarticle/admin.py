from django.contrib import admin

from myarticle import models

class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('author__username',)
    list_display = ('title', 'author')

admin.site.register(models.Article, ArticleAdmin)