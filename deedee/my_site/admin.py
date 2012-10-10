from my_site.models import Post
from my_site.models import Category
from my_site.models import Comment
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['category_name']})
                 ]
    search_fields = ['cat_name']

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['post_title', 'category']}),
                 ('Date information', {'fields': ['created_at']}),
                 ('Details', {'fields': ['post_content'], 'classes': 'collapse'})
                 ]
    list_display = ('post_title', 'created_at', 'category')
    list_filter = ['created_at']
    search_fields = ['post_title']
    date_hierarchy = 'created_at'

class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['post']}),
                 ('Date', {'fields': ['created_at']}),
                 ('Details', {'fields': ['comment_title', 'comment_content', 'comment_author']})
                 ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)