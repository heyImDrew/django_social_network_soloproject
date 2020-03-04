from rest_framework import serializers
from Thoughts.models import Post
from Communication.models import Message

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'connected_to', 'time')

class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = ('id', 'message_from', 'message_to', 'text', 'time', 'is_read')