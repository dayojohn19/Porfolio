from django.contrib.humanize.templatetags.humanize import naturalday
from django.views.decorators.csrf import csrf_exempt
import json
from user.models import Mypigeons
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Race, Entries, Lap, Mypigeons, Loaded, Record, Code, Point, Measurement, Standing
# from user.models import User
from app_mail.models import User

from django.contrib.auth.decorators import login_required
# Create your views here.

# Importing datetime.
from datetime import datetime
import datetime
# pip3 install geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time
from time import strftime, localtime


def started_race(request, rid):
    if request.method == "POST":
        update = Race.objects.get(id=rid)
        update.started = True
        update.save()
    return redirect('g_pigeon_race:manager_page')


def ended_race(request, rid):
    if request.method == "POST":
        update = Race.objects.get(id=rid)
        update.finished = True
        update.save()
    return redirect('g_pigeon_race:manager_page')


def measure(request):
    if request.method == "POST":
        place = request.POST["place"]
        xx = User.objects.get(username=request.user.username)
        mea = Nominatim(user_agent='race')
        lat = mea.geocode(place).latitude
        long = mea.geocode(place).longitude
        new_m = set()
        new_m.add(place)
        try:
            Measurement.objects.get(uid=xx.id)
        except:
            for new in new_m:
                new = Measurement(
                    uid=xx.id,
                    latitude=lat,
                    longitude=long
                )
                new.save()
        return redirect('g_pigeon_race:index')
    else:
        return redirect('g_pigeon_race:index')


def index(request):

    geolocator = Nominatim(user_agent='race')
    now = time.time()
    measured = False

# #   in seconds
#     t_time = 60
#     t_distance = 100
#     #in sec
#     t_speed = t_distance/t_time
#     # in min
#     time1=13.2
#     time2=15.1
#     d = 200
#     t1 = 1632645662.55295
#     t2 = time.time()
#     t3 = (float(t2)-float(t1)) /60
#     s = d / t3
#     # t_speed = (float(time2)-float(int(time1)))
#     t_speed = time2 - int(time1)

    if not request.user.is_authenticated:
        return redirect('user:login')
    try:
        xx = User.objects.get(username=request.user.username)
        x = Measurement.objects.get(uid=xx.id)
        measured = True
    except:
        pass
    return render(request, "race/index.html", {
        "races": Race.objects.all().order_by('id').reverse(),
        "now": now,
        # "test":t_speed,
        # "test2":str(time.strftime(" %b %d %Y, %I:%m %p ", time.localtime(time.time())))
        # "test2": time.ctime(int(time.time()))
        "test2": strftime("%I:%M:%S %p  ,  %a %b %d  %Y  ", localtime())

        #######
        #######

        # save all lap with the same id
    })


def manager(request):
    return render(request, "race/manager.html", {
        "laps": Lap.objects.filter(released=False).all().order_by('id'),
        'races': Race.objects.all().order_by('id').reverse(),
        's_races': Race.objects.filter(started=False).order_by('id').reverse(),
        'point': Point.objects.all(),
        "now": datetime.datetime.now()
    })


def start_race(request, csrf_token):
    if request.method == "POST":
        r = Race(
            racename=request.POST.get("race_name"),
            price=request.POST.get("price")
        )
        r.save()
        context = {
            'races': Race.objects.filter(finished=False).order_by('id').reverse()
        }
        # return render(request, 'race/index.html', context)
        return redirect('g_pigeon_race:manager_page')


def add_code(request, csrf_token):
    if request.method == "POST":
        code = request.POST.get("code"),
        hcode = request.POST.get("hcode")

        try:
            Code.objects.get(hcode=hcode)
            # Code.objects.get(code=code)
            return render(request, 'race/codes.html', {
                "message": "code already registered"
            })
        except:
            # x = Code.objects.get(hcode=hcode)
            # Code.objects.get(code=code)
            c = Code(
                code=request.POST.get("code"),
                hcode=request.POST.get("hcode")
            )
            c.save()
            context = {
                'cc': Code.objects.order_by('id').reverse()
            }
            return render(request, 'race/codes.html', context)
        # return redirect('g_pigeon_race:view_codes')


def add_point(request):
    if request.method == "POST":
        try:
            ll = request.POST["place"]
            lat = Nominatim(user_agent='race').geocode(ll).latitude
            long = Nominatim(user_agent='race').geocode(ll).longitude

            new_point = set()
            new_point.add(ll)
            for new in new_point:
                new = Point(
                    place=ll,
                    place_lat=lat,
                    place_long=long
                )
                new.save()
        except:
            return redirect('g_pigeon_race:manager_page')
        return redirect('g_pigeon_race:manager_page')

        # 'long':long

    # return render(request, "race/manager.html", {
    #     'lat':lat,
    #     'long':long,
    #     'new':new,
    #     'message':"New Point Saved"

    #     # 'long':long
    # })


def add_lap(request):
    if request.method == "POST":
        race_init = request.POST["race"]
        race = Race.objects.get(id=race_init)
        point_init = request.POST["point"]
        point = Point.objects.get(id=point_init)

        loading_cost = request.POST["loading_cost"]

        new_lap = set()
        new_lap.add(point)
        for n in new_lap:
            nn = Lap(
                race=race,
                release=point,
                release_lat=point.place_lat,
                release_long=point.place_long,
                loading_cost=loading_cost
            )
            nn.save()
        return HttpResponseRedirect(reverse("g_pigeon_race:add_lap"))

    return render(request, "race/lap_add.html", {
        'x': 'failed',
        'races': Race.objects.filter(finished=False),
        'point': Point.objects.all().order_by('id').reverse(),

        "laps": Lap.objects.filter(released=False).all().order_by('id'),
        'races': Race.objects.all().order_by('id').reverse(),
        's_races': Race.objects.filter(started=False).order_by('id').reverse(),

    })


def release_it(request, id):
    if request.method == "POST":
        x = Lap.objects.get(pk=id)
        x.released = True
        char_time = request.POST["release_time"]
        initial_time = time.time()
#        o = request.POST['release_timee']
        #initial_time = datetime.strptime(p, '%Y-%m-%dT%H:%M')
#        final_time = datetime.strptime(p, '%Y-%m-%dT%H:%M')
#        time_difference = initial_time - final_time
        # record.clock = str(time.strftime(" %b %d %Y, %I:%m %p ", time.localtime(time2)))
        # x.char_time = str(time.strftime(" %b %d %Y, %I:%m %p ", time.localtime(initial_time)))
        x.char_time = strftime("%I:%M:%S %p  ,  %a %b %d  %Y  ", localtime())
        # x.char_time = char_time
        x.release_time = initial_time
        x.save()

        # long = x.release_long
        # lat = x.release_lat
        Loaded.objects.filter(lap=id).update(release_time=initial_time)
        Loaded.objects.filter(lap=id).update(release_lat=x.release_lat)
        Loaded.objects.filter(lap=id).update(release_long=x.release_long)
        load = Loaded.objects.filter(lap=id).all()

        for l in load:
            l.release_time = initial_time
            l.save()
        return redirect('g_pigeon_race:release', id)
        # return render(request, "race/index.html", {
        #     "message": "released!",
        #     # "x": x,
        #     "loaded": len(load),
        #     'measured': True
        # })
    return render(request, "race/index.html", {
        "message": "released!",
        'measured': True
    })


def clock_it(request):
    if request.method == "POST":
        try:
            hcode = request.POST["clock_code"]
            loaded = Loaded.objects.get(pigeon_hcode=hcode, isLoaded=True)
            idd = loaded.pigeon_id
            loaded.clock_time = time.time()
            # remove from the loaded ##DO
            loaded.isLoaded = False
            loaded.save()
            # here get the distance
            pigeon = Mypigeons.objects.get(pk=idd)
            pigeon_id = pigeon.id
            # pigeon_name = pigeon.name
            # pigeon_ring = pigeon.ring
            # loaded_lap_id = loaded.lap
            # loaded_lap_name = loaded.lap_name
            # loaded_race = loaded.race_id
            # loaded_race_name = loaded.race_name
            # loaded_release = loaded.release_time
            loaded_clock_time = loaded.clock_time

            # loaded_speed = 321  I dont know this
            # time_get GET :
            # now = time.time()

            time1 = loaded.release_time
            time2 = time.time()
            s_time = ((time2-time1)/60)
            # minutes_time = (float(time2)-float(time1))/60
            ##              distance_get ;
            lat1 = loaded.release_lat
            long1 = loaded.release_long

            lat2 = loaded.pigeon_lat
            long2 = loaded.pigeon_long
            s_distance = geodesic((lat1, long1), (lat2, long2)).meters
            # speed_get
            s_speed = s_distance/s_time

            record = Record()
            record.pigeon_id = pigeon.id
            #  record.entry = idd
            # record.time = str(time.strftime(" %b %d %Y, %I:%m %p ", time.localtime(time.time())))
            record.time = s_time

            record.distance = s_distance
            record.ring = pigeon.ring
            record.pigeon_name = pigeon.name
            record.lap_name = loaded.lap_name
            record.lap_id = loaded.lap
            record.race = loaded.race_id
            # record.release =  time.ctime(int(loaded_release))
            # record.clock = time.ctime(int(time2))

            # record.release = str(time.strftime(" %b %d %Y, %I:%m %p ", time.localtime(loaded.release_time)))
            record.release = strftime(
                "%I:%M:%S %p  ,  %a %b %d  %Y  ", localtime(loaded.release_time))
            # record.clock = str(time.strftime(" %b %d %Y, %I:%m %p ", time.localtime(time2)))
            record.clock = strftime(
                "%I:%M:%S %p  ,  %a %b %d  %Y  ", localtime())
            # str(datetime.datetime.fromtimestamp(loaded_release))
            # record.release2 = int(loaded_release)
            # record.release = str(time.strftime(" %b %d %Y, %I:%m %p ", time.localtime(loaded_release)))
            # record.release2 = str(stry)
            record.speed = s_speed
            record.race_name = loaded.race_name
            record.save()
            record.entry.add(idd)

            # put the Mypigeons Loaded to False
            mp = Mypigeons.objects.get(id=idd)
            mp.loaded = False
            mp.save()

            # create standing
            standing = Standing.objects.get_or_create(
                race_id=loaded.race_id, pigeon_id=pigeon.id, pigeon_name=pigeon.name)

            # standing.save()
            standing = Standing.objects.get(
                race_id=loaded.race_id, pigeon_id=pigeon.id)
            standing.tspeed = +standing.tspeed + +s_speed
            standing.save()

            return render(request, "race/index.html", {
                "message": "Clocked !!",
                "x": loaded,
                "speed": s_speed,
                "xx": idd,
                "records": Record.objects.filter(entry=idd).order_by('id').reverse(),
                "count": len(Record.objects.filter(entry=idd)),
            })
        except:
            return render(request, "race/index.html", {
                "message": "You Entered Wrong Code",

            })
    else:
        return render(request, "race/index.html", {"message": "Please Enter Code"})
        # except:
        #     return render(request, "race/index.html", {"message": "Please Enter Right Code"})

    return render(request, "race/index.html", {"message": "hi you're clocked"})


def race(request, race_id):
    if not request.user.is_authenticated:
        return redirect('user:login')
    cu = request.user.username
    race = Race.objects.get(id=race_id)
    pigeons = race.registered.all().order_by('id').reverse()
    unpigeons = Mypigeons.objects.exclude(races=race.id).all().filter(
        owner=cu, loaded=False).order_by('id').reverse()
    total = len(Mypigeons.objects.filter(races=race.id))
    return render(request, "race/races.html", {
        "race": race,
        "pigeons": pigeons,
        "unpigeons": unpigeons,
        "total": total
    })


def race_registered(request, race_id):
    race = Race.objects.get(id=race_id)
    pigeons = race.registered.all().order_by('id').reverse()
    return render(request, "race/races_registered.html", {
        "race": race,
        "pigeons": pigeons
    })


def entry(request, race_id):
    if not request.user.is_authenticated:
        return redirect('user:login')
    if request.method == "POST":
        race = Race.objects.get(pk=race_id)
        pigeon_id = int(request.POST["pigeon"])
# mypigeon is to race
# record is to pigeon_id
        pigeon = Mypigeons.objects.get(pk=pigeon_id)
        pigeon.races.add(race)
        return HttpResponseRedirect(reverse("g_pigeon_race:race", args=(race.id,)))
# define clock

# get entry_id from the lap codes


def count_entry(request, id):
    pass
    # entries = Mypigeons.objects.filter(races=id)
    # return JsonResponse([pigeon.serialize() for pigeon in pigeons], safe=False)


def record(request, put_code_here):
    if request.method == "POST":
        # find the code on lap, then find the entries in lap
        entry = Entries.objects.get(pk=put_code_here)
        record_ring = entry.ring
########
        try:
            loaded = Loaded.objects.get(pigeon_hcode=put_code_here)
            record_race = loaded.race_id
            record_lap = loaded.lap
            record_release = loaded.release

            loaded.release - clock_time
            # continue
        except:
            return
######
        data = json.loads(request.body)
        record_speed = data.get("speed")
        record_lap = data.get("lap")
        record_race = data.get("race")
#        clock_ring = data.get("ring")
        x = set()
        x.add(entry)
        for e in x:
            ex = Record(
                entry=entry,
                speed=record_speed,
                ring=record_ring,
                lap=reocrd_lap,
                race=record_race
            )
            ex.save()
    return render(request, template_name)
#       clock_id = int(request.POST["clock"])
#       clock_speed = (request.POST["speed"])
#       clock_lap   = (request.POST["lap"])
#       clock_ring   = (request.POST["ring"])
#        clock_model = Clock()

#        clock = Clock.objects.get(pk=clock_id)
#        clock.entry.add(entry)

 #       clock_model.speed = clock_speed
 #       clock_model.lap   = clock_lap
  #      clock_model.ring   = clock_ring
   #     clock_model.save()


def entry2(request):
    if request.method != "POST":
        q = Entries.objects.all().order_by('id').reverse()
        return render(request, "race/entries.html", {"q": q})
    data = json.loads(request.body)
    #######
    name = data.get("name", "")
    ring = data.get("ring", "")
    code = data.get("code", "")
    link = data.get("link", "")
    owner = data.get("owner", "")
    ##time = data.get("time", "")
    x = set()
    x.add(request.user)
    for y in x:
        xy = Entries(
            user=owner,
            name=name,
            ring=ring,
            code=code,
            linkimage=link,
            ##time = time,
        )
        xy.save()

    q = Entries.objects.all()
    return render(request, "race/entries.html", {"q": q})


def remove(request, race_id):
    if request.method == "POST":
        race = Race.objects.get(pk=race_id)
        pigeon_id = int(request.POST["pigeon_id"])

        pigeon = Mypigeons.objects.get(pk=pigeon_id)
        pigeon.races.remove(race)
        return HttpResponseRedirect(reverse("g_pigeon_race:race", args=(race.id,)))


def lap(request, race_id):
    if not request.user.is_authenticated:
        return redirect('user:login')
    race = Race.objects.get(pk=race_id)
    x = request.user.username
    race = Race.objects.get(id=race_id)
    pigeons = race.registered.filter(owner=x).order_by('id').reverse()
    lap = Lap.objects.filter(
        race=race, released=False).order_by('id')
    rlap = Lap.objects.filter(
        race=race, released=True).order_by('id')
    return render(request, "race/lap.html", {
        "lap": lap,
        "rlap": rlap,
        "rn": race,
        "pigeons": pigeons,
    })


def lap_pigeon(request, rd):
    x = request.user
    race = Race.objects.get(id=rd)
    pigeons = race.registered.filter(
        owner=x, loaded=False).order_by('id').reverse()
    return JsonResponse([pigeon.serialize() for pigeon in pigeons], safe=False)


@csrf_exempt
def load_pigeon(request, pid):
    if request.method == "PUT":

        data = json.loads(request.body)
        pigeon_id = data.get("pid")
        pigeon = Mypigeons.objects.get(id=pigeon_id)
        pigeon_ring = pigeon.ring
        pigeon_name = pigeon.name
        pigeon_code = data.get("loaded_code")
        pigeon_loaded_code = data.get("loaded_code")
        lapid = data.get("lapid")
###
        pigeon2 = Mypigeons.objects.get(owner=request.user, pk=pigeon_id)

        lap_id = data.get("lapid")
        lap_name = data.get("lap_num")
# getting measurement
        xx = User.objects.get(username=request.user.username)
        my_measure = Measurement.objects.get(uid=xx.id)

        load = Loaded()
        load.race_name = data.get("race_name")
        load.race_id = data.get("race_id")
        load.lap = data.get("lap_num")
        load.pigeon_name = pigeon_name
        load.pigeon_ring = pigeon_ring
        load.lap_name = lapid
        load.pigeon_id = pigeon_id

        load.pigeon_lat = my_measure.latitude
        load.pigeon_long = my_measure.longitude
        load.pigeon_loader = request.user.username

        Code.objects.get(code=pigeon_code)
        c = Code.objects.get(code=pigeon_code)
        x = c.ring_code
        load.pigeon_hcode = c.hcode
        if x == "":
            if data.get("loaded") is not None:
                pigeon2.loaded = data["loaded"]
                pigeon2.loads = data["lapid"]
###
            c.ring_code = pigeon_ring
            c.pigeon_id = pigeon_id
            c.save()
            load.save()
            pigeon2.save()

            lp = Lap.objects.get(id=lap_name)
            lp.num_load.add(load)
            lp.save()
        else:

            return render(request, "race/lap.html", {
                "message": "message this is "})
    return HttpResponse(status=204)
    # xx = {"lap_name": aload}return render(request, "race/lap.html",xx)


def view_loaded(request, id):
    all_loaded = Loaded.objects.filter(lap=id).order_by('id').reverse()
    return render(request, "race/loaded_pigeons.html", {
        "all_loaded": all_loaded,
        "mode": "Loaded Pigeon"
    })


def view_loaded_dead(request, id):
    all_loaded = Loaded.objects.filter(
        race_id=id, isLoaded=True).order_by('id').reverse()
    return render(request, "race/loaded_pigeons.html", {
        "all_loaded": all_loaded,
        "mode": "Did not yet Return"
    })


def view_codes(request):
    cc = Code.objects.all()
    return render(request, "race/codes.html", {
        "cc": cc,
    })


def view_clocked(request, lid):
    clocked = Record.objects.filter(lap_id=lid).order_by('speed').reverse()
    lap = Lap.objects.get(id=lid)

    return render(request, "race/clocked_lap.html", {
        "time": naturalday(time.time),
        "clocked": clocked,
        "lap_name": lap.release,
        "lap_release": lap.release_time,
    })


def view_race_record(request, id):
    records = Record.objects.filter(
        race=id).order_by().values('pigeon_id').distinct()

    standings = Standing.objects.filter(race_id=id)
    # records = Record.objects.all().order_by().values('pigeon_id').distinct()

    return render(request, "race/race_record.html", {
        "records": records,
        "id": id,
        "standing": standings
    })


@csrf_exempt
def get_race_record(request):
    data = json.loads(request.body)
    race_id = data.get("race_id")
    pigeon_id = data.get("pigeon_id")
    records = Record.objects.filter(
        race=race_id, pigeon_id=pigeon_id).all().order_by('id')
    # records = Record.objects.filter(pigeon_id=pigeon_id).all().order_by('-speed')
    # records = Record.objects.filter(pigeon_id=pigeon_id).all()
    # get The TOTAL SPEED
    # for r in records:
    # r.speed
    return JsonResponse([record.serialize() for record in records], safe=False)


@csrf_exempt
def get_name(request):
    data = json.loads(request.body)
    id = data.get("x")
    names = Mypigeons
    return names
    # return JsonResponse([name.serialize() for name in names], safe=False)


def view_standing(request, id):
    standings = Standing.objects.filter(race_id=id)

    return render(request, "race/standing.html", {
        "standings": standings,
    })
