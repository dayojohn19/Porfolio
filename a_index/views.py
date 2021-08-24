# from pymongo import MongoClient
# client = pymongo.MongoClient('connection_string')
# db = client['db_name']
# connection_string = mongodb+srv://dj19:aa09094553940@cluster0.hpgnf.mongodb.net/test



###############
from django.shortcuts import render

# Create your views here.
# import pyttsx3
# import sys 
def index(request):
    # try:
    #     ar = 'Visitor'
    #     engine = pyttsx3.init()
    #     engine.say(f"Good day to you {ar}., I am a self taught Programmer., with grit., Time., and Dedication.,")
    #     engine.runAndWait(),
    #     engine.stop
    # except:
    #     pass
    return render(request, 'a_index/index.html', {})

def social(request):
    return render(request, 'social/social.html')

def colreg(request):
    return render(request, 'colregs/colregs.html')

def blog(request):
    return render(request, 'blog/blog.html')

def map(request):
    return render(request, 'map/map.html')
def games(request):
    return render(request, 'games/games.html')


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

