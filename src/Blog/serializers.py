from rest_framework import serializers
from .models import Post

class PostSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'image',
            'publish_date',
            'update_date',
            'content',
            'comment_count',
            'view_count',
            'like_count',
            'author',
            


        )