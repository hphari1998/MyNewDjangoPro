from django.contrib import admin

from commenting import models

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('author__username',)
    list_display = ('author', 'created_at', 'updated_at')

admin.site.register(models.Commentss, CommentAdmin)