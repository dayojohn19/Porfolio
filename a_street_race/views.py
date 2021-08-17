from django.shortcuts import render
from .models import Race, Room, Chat, Player
from django import forms
# Create your views here.
class NewRace(forms.Form):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Nick Name'}))
    code = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'Password Number'}))
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
                room = Room.objects.filter(full=False).get(room_code=np.code)
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
        messages = Chat.objects.filter(chat_id=room.id).order_by('id').reverse()
        return JsonResponse([message.serialize() for message in messages], safe=False)
    else:
        messages = Chat.objects.filter(chat_id=1).order_by('id')
        return JsonResponse([message.serialize() for message in messages], safe=False)
@csrf_exempt
def get_sticker(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get("code")
        player_init = data.get("player")
        player = Room.objects.filter(pk=code).get(player=player_init)
        return JsonResponse(player, safe=False)

def join(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        code = request.POST.get("code")
        host = request.POST.get("host")

        try:
            room = Room.objects.filter(full=False).get(room_code=code)
            race = Race.objects.get(code=code)
            Room.objects.filter(room_code=code).update(player2=name,full=True)
            race.delete()
            room.full = True
            return render(request, 'a_street_race/race.html',{
                'host':host,
                'player2':name,
                'code':code,
                'user':name,
                'rid':room.id,
                
            })
        except:
            room = Room.objects.filter(full=False).get(room_code=code)
            return render(request, 'a_street_race/index.html',{
                'message':'wrong Code',
                'room': Room.objects.order_by('id').reverse(),
                'rid':room.id
            })
@csrf_exempt  
def send(request):
    if request.method == 'POST':
        try:
            c = Chat()
            c.message = request.POST.get("message")
            c.chat_id = request.POST.get("chat_id")
            c.player = request.POST.get("player")
            c.save()
            return render(request, 'a_street_race/index.html',{'message':'sent'})
        except:
            data = json.loads(request.body)
            c = Chat()
            c.chat_id = data.get("chat_id")
            c.player = data.get("player")
            c.message = data.get("message_u")
            c.save()
def chat_room(request):
    pass

def sticker(request):
    if request.method == 'GET':
        room = request.GET.get("room")
        player = request.GET.get("player")
        user = request.GET.get("user")
        sticker = request.GET.get("sticker")
        ready = Room.objects.get(pk=room)
        pp = Room.objects.filter(pk=room).all()
        if player == 'player1':
            Room.objects.filter(pk=room).update(sticker1=sticker)
            return render(request, 'a_street_race/ready.html', {
                'player1': player,
                'user': user,
                '1_sticker': sticker,
                'rid':room,
                'ready': ready,
                'pp':pp
            })
        if player == 'player2':
            Room.objects.filter(pk=room).update(sticker2=sticker)
            return render(request, 'a_street_race/ready.html', {
                'player2': player,
                'user': user,
                '2_sticker': sticker,
                'rid':room,
                'ready': ready,
                'pp': pp
            })