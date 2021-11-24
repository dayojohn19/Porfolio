from django.shortcuts import render
from .models import ubx_Item
# Create your views here.


def index(request):
    return render(request, 'ubx/index.html', {
        'ubx_items': ubx_Item.objects.all(),
        'message': 'message again'
    })


def add_ubx(request):
    new = ubx_Item()
    new.first = 'test1'
    new.save()

    return render(request, 'ubx/index.html', {
        'ubx_items': ubx_Item.objects.all().order_by('id').reverse(),
        'message': new
    })
