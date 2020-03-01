from rest_framework import serializers
from Communication.models import Message

class MessageSerializer(serializers.Serializer):
    text = serializers.CharField()
    is_read = serializers.BooleanField()
    message_from_id = serializers.IntegerField()
    message_to_id = serializers.IntegerField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.is_read = validated_data.get('is_read', instance.is_read)
        instance.message_from_id = validated_data.get('message_from_id', instance.message_from_id)
        instance.message_to_id = validated_data.get('message_to_id', instance.message_to_id)
        instance.save()
        return instance