import chatterbot
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .Minor_chatbot.chatbot_runner import get_keyword
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .models import *
from django.contrib.postgres.search import SearchVector


def get_keywords(query):
    data = get_keyword(query)
    return data

# Create your views here.
def Index(request):
    return render(request, 'index.html')

#database table search
def In_About(key):
    #abt = About.objects.filter(body_text__search=key)
    abt = About.objects.annotate(search=SearchVector('body_text'),).filter(search=key)
    return abt

def In_Location(key):
    loc = Location.objects.annotate(search=SearchVector('body_text'),).filter(search=key)
    return loc

def In_Notice(key):
    noti = Notice.objects.annotate(search=SearchVector('body_text'),).filter(search=key)
    return noti

def In_Syllabus(key):
    syll = Syllabus.objects.annotate(search=SearchVector('body_text'),).filter(search=key)
    return syll


def Chat_Answer(request):
    query= request.GET['message_from_user']
    data = ""
    keyword = get_keywords(query)

    print(keyword)

    if len(keyword) == 1:
        print(keyword)
    else:
        for i in range(1, len(keyword)):
            try:

                table = keyword[i][0]
                table_key = keyword[i][1]
                print(table, ' -> ', table_key)
                if(table=="about"):
                    objectsfilterdata = In_About(table_key)

                if(table=="location"):
                    objectsfilterdata = In_Location(table_key)

                if(table=="notice"):
                    objectsfilterdata = In_Notice(table_key)

                if(table=="syllabus"):
                    objectsfilterdata = In_Syllabus(table_key)

            except:
                pass
    
    try:
        for i in objectsfilterdata:
        
            data += i.body_text 
    except:
        data = keyword

    ##search throught keywords in given table
    if data == "":
        data = "I  have no data about u asked please contact someone"

    return JsonResponse({'answer': data})


#attendance system
def Attendance(request):
    return render(request, 'index-attendance.html')


def Mark_Attendance(request):
    if request.method == 'POST':
        if request.is_ajax():
            img = request.FILES.get('imgData')
    
    
    print(img)
    data = "Attendance marked"
    print(data)

    return JsonResponse({'data': data})

