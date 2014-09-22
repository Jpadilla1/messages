from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sent_by = serializers.SlugRelatedField(slug_field='email')

    class Meta:
        model = Message
        fields = ('url', 'sent_by', 'content', 'created_at')
