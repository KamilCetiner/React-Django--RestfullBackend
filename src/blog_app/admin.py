from django.contrib import admin
from .models import Post, Like, Comment, View

# Register your models here.

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(View)