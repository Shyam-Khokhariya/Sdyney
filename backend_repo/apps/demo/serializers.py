from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'timestamp', 'user_username']

class PostSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username')
    comments = serializers.SerializerMethodField()
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'user_username', 'comment_count', 'comments']

    def get_comments(self, obj):
        # Fetch up to 3 latest comments for the post
        comments = obj.comments.order_by('-timestamp')[:3]
        return CommentSerializer(comments, many=True).data
