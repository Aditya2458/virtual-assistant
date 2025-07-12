from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
import json

# 👇 View to render the chat page
from .models import Chat
from django.shortcuts import render

def chat_view(request):
    chats = Chat.objects.order_by('created_at')  # oldest to newest
    return render(request, 'interviewbot/chat.html', {'chats': chats})


@csrf_exempt
def ai_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {settings.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are a friendly AI interviewer. Ask relevant questions and give helpful feedback."},
                {"role": "user", "content": user_message}
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            result = response.json()
            reply = result['choices'][0]['message']['content']

            # ✅ Save to database
            Chat.objects.create(question=user_message, answer=reply)

            return JsonResponse({"reply": reply})
        except Exception as e:
            print("Groq API error:", e)
            return JsonResponse({"reply": f"Error: {str(e)}"})
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Chat

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Chat

@csrf_exempt
def clear_chat(request):
    if request.method == "POST":
        Chat.objects.all().delete()
        return JsonResponse({"status": "cleared"})

