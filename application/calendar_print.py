### create an HTML formatted calendar

import calendar
from django.shortcuts import render
####
from dateutil.relativedelta import relativedelta
import datetime
from datetime import datetime
##
# import pyttsx3
##
from datetime import date
from django.views.decorators.csrf import csrf_exempt


def calendar_print(request):

    return render(request, 'application/calendar.html',{
    })
import json
@csrf_exempt
def calendar_get(request,y):
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    today = date.today()
    x=y
    st = hc.formatmonth(int(today.year), int(y))
    months = []
    for i in range(1, 13):
        months.append(calendar.month_name[i])
######
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     name = data.get('name')
    #     engine = pyttsx3.init()
    #     engine.say(f"hello, {name} How are you doing today, Welcome to my Calendar application, I hove you will like it.")
    #     try:
    #         engine.runAndWait(),
    #         engine.stop
    #     except:
    #         pass

#######
    y = y
    return render(request, 'application/calendar_stand.html',{
        'calendar': st,
        'months':months,
    })

# def calendar_script(request):
#     hc = calendar.HTMLCalendar(calendar.SATURDAY)
#     st = hc.formatmonth(2030, 2)
#     return y
    
    # render(request, 'application/calendar.html',{
    #     'calendar': st,
    #     'y':y
    # })