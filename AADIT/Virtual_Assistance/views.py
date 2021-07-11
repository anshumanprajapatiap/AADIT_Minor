import chatterbot
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .Minor_chatbot.chatbot_runner import get_keyword
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string

def get_keywords(query):
    data = get_keyword(query)
    return data

# Create your views here.
def Index(request):
  
    return render(request, 'index.html')

#database table search

def Chat_Answer(request):
    query= request.GET['message_from_user']
  
    keyword = get_keywords(query)

    ##search throught keywords in given table



    return JsonResponse({'answer': keyword})


#attendance system
def mark_attendance(request):
    pass

