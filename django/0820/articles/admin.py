from django.contrib import admin

# Register your models here.
from .models import Article
# Register your models here.


class ArticleAdimin(admin.ModelAdmin):
    list_display = (
        'title', 'content',
        'created_at', 'updated_at'
    )
    
admin.site.register(Article, ArticleAdimin)