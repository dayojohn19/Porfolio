from django.shortcuts import render
from app_Car.models import Places, PlaceSchedule
from django.shortcuts import redirect

# Create your views here.


# ALWAYS ADD EVERY RETURN
# 'navButton': carContext
carContext = {
    'allButton': [
        {'page': "/app_car/",
         'link': 'Home'},
        {'page': '/app_car/destination',
         'link': 'Make Schedules'},
        {'page': '/app_car/departure',
         'link': 'Find Schedules'},
        #  Not yet Below
        {'page': '/app_car/event',
         'link': 'Events'},
        {'page': '/app_car/complain',
         'link': 'Complaints'}

    ],
    # for faster Loading Input Destinations Here
}


def refreshSchedules(request):
    from datetime import date
    today = date.today()
    currentYear = int(today.year)
    currentDate = int(today.day)
    currentMonth = int(today.month)

    allSchedules = PlaceSchedule.objects.all()
    for i in allSchedules:
        if int(i.dateN) < currentDate:
            if int(i.monthN) <= currentMonth:
                if int(i.yearN) <= currentYear:
                    i.delete()
        if int(i.yearN) < currentYear:
            i.delete()
    return redirect('app_car:destinations')


def index(request):
    buttons = {
        'navButton': carContext,
        'appName': 'Pagong'

    }
    return render(request, 'app_car/index.html', buttons)


def departuresJSON(request):
    from django.core import serializers
    from django.http import HttpResponse

    # 'destinations': PlaceSchedule.objects.values()

    depList = PlaceSchedule.objects.order_by('-arriveTo')
    data = serializers.serialize('json', depList)
    return HttpResponse(data, content_type="application/json")


def departures(request):
    from datetime import date

    today = date.today()
    currentDate = int(today.day)
    currentMonth = int(today.month)
    currentYear = int(today.year)
    items = {
        'departures': PlaceSchedule.objects.all(),
        'currentDate': currentDate,
        'navButton': carContext,
        'currentMonth': currentMonth,
        'currentYear': currentYear
    }
    return render(request, 'app_car/departure.html', items)


def destinations(request):
    from datetime import date
    today = date.today()

    items = {
        'navButton': carContext,
        'allDestinations': Places.objects.all(),
        'currentMonth': int(today.month),

    }
    if request.method == 'POST':
        try:
            place = request.POST.get('place')
            if place == '':
                return redirect('app_car:destinations')
            newPlace = Places.objects.create(placename=place)

            from datetime import date
            currentMonth = int(today.month)

            newPlace.save()

            return redirect('app_car:place', newPlace.id, currentMonth)

        except:
            return redirect('app_car:destinations')

    # return redirect('app_car:index')
    return render(request, 'app_car/destination.html', items)


def place(request, id, currentMonth):
    from .forms import PlaceScheduleForm, PlaceEventForm
    #
    import calendar
    from datetime import date
    thisMonth = calendar.HTMLCalendar(calendar.FRIDAY)
    today = date.today()
    # currentMonth = int(today.month)

    currentDate = int(today.day)
    currentYear = int(today.year)

    if (currentMonth >= 13):
        currentMonth = 1
        currentYear += 1

    elif (currentMonth <= 0):
        currentMonth = 12
        currentYear -= 1

    showCalendar = thisMonth.formatmonth(currentYear, currentMonth)
    place = Places.objects.get(pk=id)

    newEventForm = PlaceEventForm()
    newScheduleForm = PlaceScheduleForm()

    #
    context = {
        'calendar': showCalendar,
        'place': place,
        'navButton': carContext,
        'numberN': 12,
        'newSchedForm': newScheduleForm,
        'newEventForm': newEventForm,
        'currentMonth': currentMonth,
        'currentDate': currentDate,
        'nextMonth': currentMonth+1,
        'previousMonth': int(currentMonth)-1,
        'currentYear': currentYear
    }

    if request.method == 'POST':
        newFormform = PlaceScheduleForm(request.POST)
        if newFormform.is_valid():
            depTime = request.POST.get('departTime')
            depDate = request.POST.get('departDate')
            depDate = depDate.split('-')
            newFormform.instance.yearN = depDate[0]
            newFormform.instance.dateN = depDate[2]
            newFormform.instance.monthN = depDate[1]
            newFormform.instance.timeDeparture = request.POST.get('departTime')
            newFormform.save()
            place.placeSchedule.add(newFormform.instance)
            newFormform.instance.arriveTo = place
            newFormform.save()
            return redirect('app_car:place', id, currentMonth)

        return render(request, 'app_car/place.html', context)

    return render(request, 'app_car/place.html', context)


def PlaceAddEvent(request, id, currentMonth):
    from .forms import PlaceEventForm
    place = Places.objects.get(pk=id)
    if request.method == 'POST':
        newEventForm = PlaceEventForm(request.POST)
        if newEventForm.is_valid():
            newEventForm.save()
            place.placeEvent.add(newEventForm.instance)
            newEventForm.instance.eventPlace = place
            newEventForm.save()
            return redirect('app_car:place', id, currentMonth)
