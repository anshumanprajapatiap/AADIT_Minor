import chatterbot
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .Minor_chatbot.chatbot_runner import get_keyword


def get_keywords(query):

    data = get_keyword(query)
    return data

# Create your views here.
def Index(request):
    now = datetime.datetime.now()

    #data from user
    query = "class of arpit sir"

    keyword = get_keywords(query)
    print(keyword)
    html = "<html><body>It is now %s.</body></html>" % keyword
    return HttpResponse(html)

#database table search




#attendance system
def mark_attendance(request):
    pass

