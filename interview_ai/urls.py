"""
URL configuration for interview_ai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path
from interviewbot.views import chat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_view, name='chat'),
]
from interviewbot.views import chat_view, ai_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_view, name='chat'),
    path('ai-response/', ai_response, name='ai_response'),
]
