from django.contrib import admin
from .models import Author, Category, Post, PostInstance

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostInstance)