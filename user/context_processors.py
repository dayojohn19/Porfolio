from com_sale.models import Order
from app_mail.models import User
from com_auction.models import Watchlist, Closedbid
from django.shortcuts import render,redirect

def add_variable_to_context(request):
    try:
        orders = Order.objects.filter(user=request.user).order_by('id').reverse()
        buyers = Order.objects.filter(owner=request.user, delivered=False).order_by('id').reverse()
        watches = Watchlist.objects.filter(user= request.user.username)
        closed = Closedbid.objects.filter(winner = request.user.username)
        watchlist = Watchlist.objects.filter(user=request.user.username)
        return {
            'orders':len(orders),
            'buyers':len(buyers),
            'users':User.objects.all(),
            'closed': len(closed),
            'watches':watches,
            'wcount':len(watchlist)
        }
    except:
        return {}