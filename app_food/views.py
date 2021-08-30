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
        user = request.POST.get('user')
        am = 0
        pm = 0
        eve = 0
        if request.POST.get('AM'):
            am = request.POST.get('AM')
        if request.POST.get('PM'):
            pm = request.POST.get('PM')
        if request.POST.get('EVE'):
            eve = request.POST.get('EVE')
        
        tt = Tally(
            user = user,
            am = am,
            pm = pm,
            eve = eve,
            ### cost
            cost = int(am)+int(pm)+int(eve)
        )
        tt.save()
        context = {
            'foods': Tally.objects.all().order_by('id').reverse(),
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
        return render(request, "application/food/cook.html", context)
    else:
        return render(request, "application/food/cook.html", {
            'message':'please complete the form',
            'n': len(Food.objects.filter(date=current_time))
            })