from django.contrib import admin
from core.models import Article

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'created_at')


admin.site.register(Article, ArticleAdmin)

