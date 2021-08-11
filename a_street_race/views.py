from django.shortcuts import render
from .models import Race, Room, Chat
from django import forms
# Create your views here.
class NewRace(forms.Form):
    name = forms.CharField(label="Nick Name")
    code = forms.IntegerField(label="Room Password")
def index(request):
    return render(request, 'a_street_race/index.html', {
        'room': Room.objects.filter(full=False).order_by('id').reverse(),
        'form':NewRace()
    })
def race(request):
    return render(request, 'a_street_race/race.html')

def create(request):
    if request.method == 'POST':
        form = NewRace(request.POST)
        if form.is_valid():
            form.cleaned_data["name"]
            form.cleaned_data["code"]
            ncode= request.POST.get("code")
            np = Race()
            np.host = request.POST.get("name")
            np.code = request.POST.get("code")
            rm = Room()
            rm.player1 = np.host
            rm.room_code = np.code
            try:
                Race.objects.get(code=ncode)
                room = Room.objects.get(room_code=np.code)
                return render(request, 'a_street_race/race.html',{
                'host':rm.player1,
                'code':rm.room_code,
                'player2':room.player2,
                'rid':room.id,
                'message':'done',
                'user':np.host
            })
            except:
                np.save()
                rm.save()
                room = Room.objects.get(room_code=np.code)
                return render(request, 'a_street_race/race.html',{
                    'rid':room.id,
                    'host':rm.player1,
                    'code':rm.room_code,
                    'message':'new',
                    'player2':rm.player2,
                    'user':np.host
                })
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
@csrf_exempt
def fetch(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')
        room = Room.objects.get(room_code=code)
        re = room.player2
        return JsonResponse(re, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        code = data.get('code')
        room = Room.objects.get(room_code=code)
        ch = Chat.objects.filter(chat_id=room.id).order_by('id').reverse()
        return JsonResponse(ch, safe=False)
def join(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        code = request.POST.get("code")
        host = request.POST.get("host")

        try:
            room = Room.objects.get(room_code=code)
            Room.objects.filter(room_code=code).update(player2=name,full=True)
            return render(request, 'a_street_race/race.html',{
                'host':host,
                'player2':name,
                'code':code,
                'user':name,
                'rid':room.id
            })
        except:
            room = Room.objects.get(room_code=code)
            return render(request, 'a_street_race/index.html',{
                'message':'wrong Code',
                'room': Room.objects.order_by('id').reverse(),
                'rid':room.id
            })
            
def send(requesst):
    if request.method == 'POST':
        message = request.POST.get("message_u")
        player = request.POST.get("player")
        chat_id = request.POST.get("chat_id")