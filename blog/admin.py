from django.contrib import admin

# Register your models here. Thank you

from . models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title', 'slug', 'author_id', 'author', 'publish', 'status']
    list_filter=['status', 'created', 'publish']
    search_fields=['title', 'body']
    date_hierarchy='publish'
    prepopulated_fields={'slug':['title']}