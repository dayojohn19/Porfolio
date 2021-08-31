from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .models import Tally , Food 
from django.urls import reverse



from datetime import datetime
# for timezone()
import pytz
  

# Create your views here.
def index(request):
    now = datetime.now()
    current_time = now.strftime("%d%m")
  
    context = {
        'today': Food.objects.filter(date=current_time).order_by('id').reverse(),
    }
    return render(request, 'application/food/index.html', context)

def submit(request):
    if request.method == 'POST':
        user = request.user.username
        am = 0
        pm = 0
        eve = 0
        if request.POST.get('AM'):
            am = request.POST.get('AM')
        if request.POST.get('PM'):
            pm = request.POST.get('PM')
        if request.POST.get('EVE'):
            eve = request.POST.get('EVE')
        now = datetime.now()
        current_time = now.strftime("%d%m")
  
        tt = Tally(
            date = current_time,
            user = user,
            am = am,
            pm = pm,
            eve = eve,
            ### cost
            cost = int(am)+int(pm)+int(eve)
        )
        zz = 0
        try:
            Tally.objects.get(user=user)
            zz = ' You already registered'
        except:
            tt.save()
        # if 'npr' in zz.user.all() :
        #     x = 'already'
        # else:
        #     
        #### solve all 
        all_cost = Tally.objects.filter(date=current_time)
        z = []
        for a in all_cost:
            z.append(int(a.cost))
        s = sum(z)
                
        context = {
            'foods': Tally.objects.filter(date=current_time).order_by('id').reverse(),
            'yy':zz,
            'sum':s
            # 'filter': Tally.objects.filter()
        }
        return render(request, "application/food/tally.html",context)
            
    # else:
    #     return HttpResponseRedirect(reverse("food:index"))

def cook(request):
    now = datetime.now()
    current_time = now.strftime("%d%m")
    if request.method == 'POST':
        date = request.POST.get('date')
        umaga = request.POST.get('umaga')
        tanghali = request.POST.get('tanghali')
        gabi = request.POST.get('gabi')
        u_cost = request.POST.get('umaga_cost')
        t_cost = request.POST.get('tanghali_cost')
        g_cost = request.POST.get('gabi_cost')
        cook = request.user.username
        ff = Food(
            date = request.POST.get('date'),
            umaga = request.POST.get('umaga'),
            tanghali = request.POST.get('tanghali'),
            gabi = request.POST.get('gabi'),
            u_cost = u_cost,
            t_cost = t_cost,
            g_cost = g_cost,
            cook = cook
        )
        n = len(Food.objects.filter(date=current_time))
        if n >= 1:
            Food.objects.filter(date=current_time).update(
                umaga=umaga, tanghali=tanghali, gabi=gabi, u_cost = u_cost,t_cost = t_cost,g_cost = g_cost,)
        else:
            ff.save()
        context = {
            'today': Food.objects.filter(date=request.POST.get('date')).order_by('id').reverse(),
            'n': len(Food.objects.filter(date=current_time))
        }
        return render(request, "application/food/index.html", context)
    else:
        return render(request, "application/food/cook.html", {
            'message':'please complete the form',
            'n': len(Food.objects.filter(date=current_time))
            })


from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from app_mail import models as mail
def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "application/mail/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = mail.User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "application/mail/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("food:index"))
    else:
        return HttpResponseRedirect(reverse("food:index"))

