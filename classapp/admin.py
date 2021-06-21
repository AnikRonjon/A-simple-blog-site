from django.contrib import admin
from .models import Category, Post


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'published', 'image')
    list_filter = ('author', 'category')
    search_fields = ('title', 'body', 'author', 'category')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published'
