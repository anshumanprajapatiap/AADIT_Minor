from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "Virtual_Assistance"

urlpatterns = [
    path('', Index, name='Index'),
    path('chat-bot/', Chat_Answer, name='Chat_Answer')

]