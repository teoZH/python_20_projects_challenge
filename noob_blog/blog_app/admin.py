from django.contrib import admin
from blog_app.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date')
    prepopulated_fields = {
        'slug': ('title',)
    }
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)