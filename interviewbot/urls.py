from django.urls import path
from .views import chat_view, ai_response, clear_chat

urlpatterns = [
    path('', chat_view, name='chat'),
    path('ai-response/', ai_response, name='ai_response'),
    path('clear-chat/', clear_chat, name='clear_chat'),
    

]
