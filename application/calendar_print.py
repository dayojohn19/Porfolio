### create an HTML formatted calendar

import calendar
from django.shortcuts import render
####
from dateutil.relativedelta import relativedelta
import datetime
from datetime import datetime


from datetime import date
from django.views.decorators.csrf import csrf_exempt


def calendar_print(request):

    return render(request, 'application/calendar.html',{
    })

@csrf_exempt
def calendar_get(request,y):
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    today = date.today()
    # if request.POST == 'POST':
    #     y = request.POST.get("month", False)
    #     st = hc.formatmonth(int(today.year), int(y))
    # else:
    st = hc.formatmonth(int(today.year), int(y))
    months = []
    for i in range(1, 13):
        months.append(calendar.month_name[i])
    #
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