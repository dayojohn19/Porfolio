import sys 

from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import ImageForm, UserImageForm
from user.models import Chain
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import pytz
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Mypigeons, Order, User_Coins, User_visitor
from g_pigeon_race.models import Record
from geopy.geocoders import Nominatim
# xx = User.objects.get(username=request.user.username)

# get user as mail.User
from app_mail import models as mail
###
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_user_ip(request):
    # add option updating USER LOCATION and CONTACT and DURATION
    print('Getting User Ip....')
    try:
        import ssl  # adding certificate
        import urllib.request
        import requests
        ssl._create_default_https_context = ssl._create_unverified_context  # adding certificate
        external_ip = urllib.request.urlopen(
            'https://ident.me').read().decode('utf8')
        your_ip = external_ip
        try:
            print('Visiting...')
            visitor = User_visitor.objects.get(ip=your_ip)
            visitor.visit_count += 1
            visitor.save()
            try:
                if not visitor.contact:
                    if request.method == 'POST':
                        data = json.loads(request.body)
                        print(data['contact'])
                        contact = data['contact']
                        visitor.contact = contact
                        visitor.save()
                    # ADD SEND EMAIL at Python FOLDER send_email
                    return JsonResponse(visitor.contact, safe=False)
            except:
                return JsonResponse('get_contact', safe=False)

            print('Visited')
            return JsonResponse(your_ip, safe=False)
        except:
            print('First Time Visiting...')
            your_location = requests.get(
                f"https://geolocation-db.com/json/{your_ip}&position=true").json()
    #   ADDRESS
            geoLoc = Nominatim(user_agent="GetLoc")
            user_long = your_location['longitude']
            user_lat = your_location['latitude']
            your_address = geoLoc.reverse(f"{user_lat}, {user_long}")
            #
            new_vistor = User_visitor()
            new_vistor.location = your_location
            new_vistor.ip = your_ip
            new_vistor.address = your_address
            new_vistor.visit_count = 1
            new_vistor.save()
            print('Visited ')
            print('your Address: ', your_address)
            print(your_location['country_name'])
            print(your_ip)

            # visitor = User_visitor.objects.get(ip=1)

            return JsonResponse(your_ip, safe=False)
    except:
        print('FAIL')
        # new_visitor = User_visitor()
        # new_visitor.address =
        # new_visitor.location =
        return JsonResponse('no_ip', safe=False)
        # return print('False')


def send_email(request):
    from django.core.mail import send_mail
    from webpage import settings
    subject = "Greetings"
    msg = "Congratulations for your success"
    to = "dayo_john16@yahoo.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)


def get_pdf(request):
    from reportlab.pdfgen import canvas
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100, 700, "Hello, Javatpoint.")
    p.showPage()
    p.save()
    return response


def get_csv(request):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    employees = Mypigeons.objects.all()
    writer = csv.writer(response)
    for employee in employees:
        writer.writerow([employee.owner, employee.name, employee.ring])
    writer.writerow(['first', 'SECOND', '3333'])
    writer.writerow(['first', 'SECOND', '3333'])

    return response


def send_sms(request):
    from sms import send_sms

    send_sms(
        'Here is the message',
        '+639568543802',
        ['+639568543802'],
        fail_silently=False
    )


def printit(request):
    from . import transactions
    transactions.Transfer()
    return JsonResponse(transactions.Transfer(), safe=False)


def Order_it(request):
    if request.method == 'POST':
        sell_coin = request.POST.get("sell_coin")
        buy_coin = request.POST.get("buy_coin")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        side = request.POST.get("side")
        user_id = request.user.id
    from . import transactions
    transactions.fill_order(sell_coin, buy_coin,
                            quantity, price, user_id, side)
    print(sell_coin, buy_coin, quantity, price, side)
    return redirect('user:userpage')


@csrf_exempt
def Js_Order_it(request):
    if request.method != "POST":
        return JsonResponse('error', status=400)
    data = json.loads(request.body)
    quantity = data.get("quantity")
    price = data.get("price")
    side = data.get("side")
    sell_coin = data.get("sell_coin")
    buy_coin = data.get("buy_coin")
    user_id = request.user.id
    # try:
    if side == 'cancel':
        from . import transactions
        transactions.cancel_order(
            user_id, sell_coin, buy_coin, quantity, price, side)
    # return JsonResponse('CANCEL', safe=False)

    #     elif side == 'buy':
    #         return JsonResponse('BUY', safe=False)

    #     elif side == 'sell':
    #         return JsonResponse('SELL', safe=False)

    #     return JsonResponse('Success', safe=False)
    # except:
    #     return JsonResponse('Failed', safe=False)
    from . import transactions
    val = transactions.fill_order(sell_coin, buy_coin,
                                  quantity, price, user_id, side)
    print(sell_coin, buy_coin, quantity, price, side)
    print(val)
    return JsonResponse('SUCCESS,  page reloading....', safe=False)


def Cancel_it(request):
    if request.method == 'POST':
        sell_coin = request.POST.get("sell_coin")
        buy_coin = request.POST.get("buy_coin")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        side = request.POST.get("side")
        user_id = request.user.id
    from . import transactions
    transactions.cancel_order(
        user_id, sell_coin, buy_coin, quantity, price, side)
    print('order has been canceled')
    return redirect('user:userpage')


# @csrf_exempt
# def tradeIt(request):
#     if request.method != "POST":
#         return JsonResponse('error', status=400)
#     data = json.loads(request.body)
#     quantity = data.get("quantity")
#     coin = data.get("coin")
#     price = data.get("price")

#     user_id = data.get("user_id")
#     balance = data.get("balance")
#     hashed = data.get("hash")
#     try:
#         user = mail.User.objects.get(
#             id=user_id, last_name=balance, first_name=hashed)
#         from . import transactions
#         result = transactions.Trade_it(
#             user_id, balance, hashed, quantity, coin, price)
#         return JsonResponse(result, safe=False)
#     except:
#         return JsonResponse('failed', safe=False)

#     # from . import transactions
#     # transactions.Trade_it()
#     # return JsonResponse(transactions.Trade_it(), safe=False)


def user_page(request):
    sell_coin = 'dcoin'
    buy_coin = 'jcoin'
    coins = User_Coins.objects.all()
    sell_remaining = coins.filter(coin=sell_coin)
    buy_remaining = coins.filter(coin=buy_coin)

    sell_quantity = 0
    buy_quantity = 0
    for s in sell_remaining:
        sell_quantity += s.quantity
    for b in buy_remaining:
        buy_quantity += b.quantity

    return render(request, "user/userPage.html",
                  {
                      'orders': Order.objects.all(),
                      'coins': coins,
                      'sell_remaining': sell_quantity,
                      'sell_coin': sell_coin,
                      'buy_coin': buy_coin,
                      'buy_remaining': buy_quantity
                  })


def player(request, username):
    if request.method == 'GET':
        xx = mail.User.objects.get(username=request.user.username)

        viewer = request.user.username
        viewing = get_object_or_404(mail.User, username=username)
        viewing_pic = mail.User.objects.get(username=username)
        lists = Mypigeons.objects.filter(
            owner=viewing).order_by('id').reverse()
        c = len(lists)

        if request.user.is_anonymous:
            return render(request, "user/login.html")
            # return redirect('user:login')
        else:
            return render(request, "user/player.html", {
                'list': lists,
                'lo': viewing,
                'c': c,
                'pic': viewing_pic.email
            })


def addpigeon(request):
    if request.method == "POST":
        # add time
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
        lists = Mypigeons.objects.filter(
            owner=viewing).order_by('id').reverse()

        return redirect('g_pigeon_race:index')


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
            return render(request, 'user/add.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'user/add.html', {'form': form})


@csrf_exempt
def userpictures(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'user/register.html', {'form': form, 'img_obj': img_obj})
    else:
        form = UserImageForm()
    return render(request, 'user/register.html', {'form': form})


def index(request):
    if request.user.is_anonymous:
        next = request.path
        return render(request, "user/login.html", {'next': next})

        # return redirect('user:login')
        # return render(request, "user/login.html")
    user = request.user
    bb = mail.User
    users = bb.objects.all().order_by('id').reverse()
    count = len(bb.objects.all())
    return render(request, "user/index.html", {
        "l": user,
        "au": users,
        "user_count": count
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        next = request.POST.get('next', '/')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
            # return HttpResponseRedirect(reverse("user:index"))
        else:
            return render((request), "user/login.html", {"message": "invalid username and/or password."})
    else:

        # return render(request, "user/login.html", {'next': next})
        return HttpResponseRedirect(reverse("user:index"))

        # return render(request, "a_index/index.html")


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
        return HttpResponseRedirect(reverse("user:index"))
    else:
        form = UserImageForm()
        return render(request, "user/register.html",
                      {'form': form})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "user/register.html", {"message": "Passwords must match."})
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

        return render(request, "user/register.html", {'form': form})


def view_record(request, pid):
    # change 195 to pigeon id
    mp = Mypigeons.objects.get(id=pid)
    mpl = mp.link
    name = mp.name
    z1 = mp.id
    zz = mp.entry.all().order_by('id').reverse()
    return render(request, "user/pigeon_record.html", {
        "records": Record.objects.filter(entry=pid).order_by('id').reverse(),
        "count": len(Record.objects.filter(entry=pid)),
        "zz": zz,
        "mpl": mpl,
        'pid': name
    })


# chain coin


def last_name(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        lastname = request.POST.get("last_name")
        requestToChain = user.first_name

        # get block
        try:
            block = Chain.objects.get(chain=requestToChain)
            value = block.value
            # x.delete()
            user.first_name = hash(str(value))
            user.last_name = value + lastname
            user.save()
            # create new block
            b = Chain()
            b.chain = hash(str(value))
            b.value = value + lastname
            b.save

        # create block
        except:
            x = 'noned'
            c = Chain()
            c.chain = user.first_name
            c.value = lastname
            c.save()

    return render(request, 'commerce/commerce.html', {
        'new': User.objects.get(pk=request.user.id),
        'last': user.last_name,
        'first': user.first_name,
        'chains': Chain.objects.all(),
        # 'x':x
    })
