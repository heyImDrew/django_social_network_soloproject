from rest_framework import serializers
from Thoughts.models import Post, Comment
from Communication.models import Message

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'connected_to', 'time')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'connected_to', 'connected_to_post')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message_from', 'message_to', 'text', 'time', 'is_read')