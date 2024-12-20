from com_sale.models import Order
from app_mail.models import User
from com_auction.models import Watchlist, Closedbid
from django.shortcuts import render, redirect
from user.models import User_Coins


def add_variable_to_context(request):
    try:
        orders = Order.objects.filter(
            user=request.user).order_by('id').reverse()
        buyers = Order.objects.filter(
            owner=request.user, delivered=False).order_by('id').reverse()
        watches = Watchlist.objects.filter(user=request.user.username)
        closed = Closedbid.objects.filter(winner=request.user.username)
        watchlist = Watchlist.objects.filter(user=request.user.username)
        you_coins = User_Coins.objects.filter(user_id=request.user.id)
        
        visited = 1
        return {
            'visited': visited,
            'orders': len(orders),
            'buyers': len(buyers),
            'users': User.objects.all(),
            'closed': len(closed),
            'watches': watches,
            'wcount': len(watchlist),
            'your_coins': you_coins
        }
    except:
        return {}
