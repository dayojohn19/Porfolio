# from pymongo import MongoClient
# client = pymongo.MongoClient('connection_string')
# db = client['db_name']
# connection_string = mongodb+srv://dj19:aa09094553940@cluster0.hpgnf.mongodb.net/test


###############
from django.shortcuts import render

# Create your views here.
import pyttsx3
import sys
from django.shortcuts import render
from .models import Item
from app_mail import models as recepient
from django.http import HttpResponse


def path(request, path):
    return HttpResponse(f"Requested Path: {path}")


def index(request):
    try:
        ar = 'Visitor'
        engine = pyttsx3.init()
        engine.say(
            f"Good day to you {ar}., I am a self taught Programmer., with grit., Time., and Dedication.,")
        engine.runAndWait(),
        engine.stop
    except:
        pass
    return render(request, 'a_index/index.html')


def send(request):
    if request.method != "POST":
        return render(request, 'a_index/index.html')
    users = set()
    for user in users:
        sent = recepient.Email(
            user='m@l.com',
            sender='random@l.com',
            subject='I like Your Post',
            body=request.POST.get("body"),
        )
        sent.save()
    return render(request, 'a_index/index.html')


def social(request):
    obj = Item.objects.all()
    return render(request, 'social/social.html', {'obj': obj})


def colreg(request):
    return render(request, 'colregs/colregs.html')


def games(request):
    return render(request, 'games/games.html')


def s(request):
    return render(request, 'social/s.html')


def fish(request):
    return render(request, 'fish/index.html')


def commerce(request):
    return render(request, 'commerce/commerce.html')

# import json
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def speech(request,y):
# ######
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         name = data.get('name')
#         engine = pyttsx3.init()
#         engine.say(f"hello, {name} How are you doing today, Welcome to my Calendar application, I hove you will like it.")
#         try:
#             engine.runAndWait(),
#             engine.stop
#         except:
#             pass
