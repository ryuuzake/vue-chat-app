from django.urls import path, include
from rest_framework.routers import DefaultRouter

from chat import views

# Create Default Router and Register ViewSet
router = DefaultRouter()
router.register(r'chats', views.ChatViewSet, basename='chat')

urlpatterns = [
    path('', include(router.urls)),
    path('chats/<int:pk>/messages/', views.MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='chat-messages'),
]
