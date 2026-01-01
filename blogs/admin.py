from django.contrib import admin
from .models import Blog, Category, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured', 'created_at')
    search_fields = ('title', 'status','author__username', 'category__category_name')
    list_editable = ('is_featured',)
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)