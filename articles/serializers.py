from rest_framework import serializers
from .models import Articles, Comment

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    class Meta:
        model = Articles
        fields = ("id", "title", "content", "created_at", "updated_at", "user")

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    ariticles = serializers.ReadOnlyField(source = "articles.pk")
    comment_pk = serializers.ReadOnlyField(source = "comment.pk")

    class Meta:
        model = Comment
        fields = ("id", "ariticles", "content", "created_at", "updated_at", "user", "comment_pk")
