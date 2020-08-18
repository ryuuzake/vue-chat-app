from rest_framework import viewsets
from rest_framework.response import Response
from chat import serializers, models

# Create your views here.
class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChatSerializer
    paginator = None

    def get_queryset(self):
        return models.Chat.objects.filter(users=self.request.user)
    

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer
    paginator = None

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return models.Message.objects.filter(chat=self.kwargs['pk'])

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset.update(status=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    
