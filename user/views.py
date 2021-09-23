from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Mypigeons
from g_pigeon_race.models import Record
from geopy.geocoders import Nominatim
# xx = User.objects.get(username=request.user.username)

## get user as mail.User
from app_mail import models as mail
###
def player(request, username):
    if request.method == 'GET':
        xx = mail.User.objects.get(username=request.user.username)

        viewer = request.user.username
        viewing = get_object_or_404(mail.User, username=username)
        viewing_pic = mail.User.objects.get(username=username)
        lists = Mypigeons.objects.filter(owner=viewing).order_by('id').reverse()
        c = len(lists)


        if request.user.is_anonymous:
            return redirect('user:login')
        else:
            return render(request, "user/player.html", {
                'list':lists,
                'lo':viewing,
                'c':c,
                'pic':viewing_pic.email
            })

from .forms import ImageForm, UserImageForm
import pytz
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

def addpigeon(request):
    if request.method == "POST":
        #add time
        ltz = pytz.timezone('Asia/Manila')
        now = datetime.now(ltz)
        dt = now.strftime("%A %d %B %Y %X")

        np = Mypigeons()
        np.owner = request.user.username
        np.name = request.POST.get('name')
        np.ring = request.POST.get('ring')
        np.link = request.POST.get('link')
        np.time = dt
        ring = np.ring

        try:
            Mypigeons.objects.get(ring=ring)
            return render(request, "user/player.html", {'error': ring, 'error2': "Ring already registered"})
        except:
            np.save()
        username = request.user.username
        viewer = request.user.username
        viewing = get_object_or_404(mail.User, username=username)
        lists = Mypigeons.objects.filter(owner=viewing).order_by('id').reverse()

        return redirect('g_pigeon_race:index')

from django.http import JsonResponse
import json
@csrf_exempt
def load_pigeon(request, id):
    if request.method == "PUT":
        pigeon = Mypigeons.objects.get(owner=request.user, pk=id)
        data = json.loads(request.body)
        if data.get("loaded") is not None:
            pigeon.loaded = data["loaded"]
            pigeon.loads = data["lapid"]
        pigeon.save()
        return HttpResponse(status=204)


      


@csrf_exempt
def pictures(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'user/add.html', {'form':form, 'img_obj':img_obj})
    else:
        form = ImageForm()
    return render(request, 'user/add.html', {'form':form})
@csrf_exempt
def userpictures(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'user/register.html', {'form':form, 'img_obj':img_obj})
    else:
        form = UserImageForm()
    return render(request, 'user/register.html', {'form':form})

def index(request):
    if request.user.is_anonymous:
        return redirect('user:login')
    user = request.user
    bb = mail.User
    users = bb.objects.all().order_by('id').reverse()  
    count = len(bb.objects.all())
    return render(request, "user/index.html",{
        "l":user,
        "au":users,
        "user_count": count 
        })
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("user:index"))
        else:
            return render((request), "user/login.html", {"message": "invalid username and/or password."})
    else:
        return render(request, "user/login.html")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("user:index"))

def register_sec(request):
    if request.method == "POST":
        username = request.POST["email"]
        email = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "user/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = mail.User.objects.create_user(
                username,
                email,
                password
            )
            user.last_name = 1
            user.first_name = 1
            user.save()
        except IntegrityError:
            return render(request, "user/register.html", {
                "message": "Username already taken. "
            })
        login(request, user)
        return HttpResponseRedirect(reverse("sale:index"))
    else:
        form = UserImageForm()
        return render(request, "user/register.html",
        {'form':form})

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "user/register.html", { "message": "Passwords must match."})
        try:
            user = mail.User.objects.create_user(
                username,
                email,
                password
            )
            user.last_name = 1000
            user.first_name = 1000
            user.save()
        except IntegrityError:
            return render(request, "user/register.html", {"message": "Username already taken."})


        login(request, user)
        return HttpResponseRedirect(reverse("user:index"))
    else:
        form = UserImageForm()

        return render(request, "user/register.html",{'form':form})


def view_record(request, pid):
#change 195 to pigeon id
    mp = Mypigeons.objects.get(id=pid)
    mpl = mp.link
    name = mp.name
    z1 = mp.id
    zz = mp.entry.all().order_by('id').reverse()
    return render(request, "user/pigeon_record.html", {
        "records": Record.objects.filter(entry=pid).order_by('id').reverse(),
        "count": len(Record.objects.filter(entry=pid)),
        "zz":zz,
        "mpl": mpl,
        'pid': name
    })


### chain coin
from user.models import Chain
def last_name(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        lastname = request.POST.get("last_name")
        requestToChain = user.first_name

        ## get block
        try:
            block = Chain.objects.get(chain=requestToChain)
            value = block.value
            # x.delete()
            user.first_name = hash(str(value))
            user.last_name = value + lastname
            user.save()
            ## create new block
            b = Chain()
            b.chain = hash(str(value))
            b.value = value + lastname
            b.save

        ## create block
        except:
            x = 'noned'
            c = Chain()
            c.chain = user.first_name
            c.value = lastname
            c.save()
        
    return render(request, 'commerce/commerce.html', {
        'new':User.objects.get(pk=request.user.id),
        'last':user.last_name,
        'first':user.first_name,
        'chains':Chain.objects.all(),
        # 'x':x
    })
