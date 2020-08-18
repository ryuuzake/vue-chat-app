from rest_framework import serializers

from chat import models

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    from_user = serializers.CurrentUserDefault()

    class Meta:
        model = models.Message
        fields = '__all__'
