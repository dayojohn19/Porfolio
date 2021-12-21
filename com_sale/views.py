from .forms import ImageForm, UserImageForm
from django.shortcuts import render
from django import forms
from com_sale.models import Item, Order
from django.shortcuts import redirect
from django.http import HttpResponse
from app_mail.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.db import IntegrityError

from datetime import date, time, datetime, timedelta
# from datetime import time
# from datetime import datetime
# from datetime import timedelta

import datetime


def category(request, category):
    orders = Order.objects.filter(user=request.user).order_by('id').reverse()
    categorized = Item.objects.filter(
        category=category).order_by('id').reverse()
    contents = {
        'item': categorized,
        'orders': len(orders)
    }
    return render(request, 'commerce/sale/index.html', contents)


def mylist(request):
    orders = Order.objects.filter(user=request.user).order_by('id').reverse()
    filtered = Item.objects.filter(owner=request.user).order_by('id').reverse()
    contents = {
        'items': filtered,
        'orders': len(orders)
    }
    return render(request, 'commerce/sale/mylist.html', contents)


def myorder(request):
    filtered = Order.objects.filter(user=request.user).order_by('id').reverse()
    contents = {
        'items': filtered
    }
    return render(request, 'commerce/sale/myorder.html', contents)


def mybuyer(request):
    # Post Deliver
    if request.method == 'POST':
        item_id = request.POST.get("item_id")
        x = Order.objects.get(id=item_id)
        user = x.user
        order = Item.objects.get(id=x.i_id)
        order_price = int(order.price) * int(x.qty)
        add_check(request.user, request.user.first_name, order_price)
        if user in order.orders.all():
            o = Order.objects.get(item=order, user=user, delivered=False)
            o.delete()
            order.orders.remove(user)
            order.bought = int(order.bought) + int(x.qty)
            order.save()
            x.delivered = True
            x.del_time = datetime.datetime.now()
            x.save()
            return redirect('sale:mybuyer')
    # end POST deliver
    filtered = Order.objects.filter(
        owner=request.user).order_by('id').reverse()
    contents = {
        'items': filtered,
        'date': datetime.datetime.now()
    }
    return render(request, 'commerce/sale/mybuyer.html', contents)


def add_check(user, hashed, i_price):
    # update value
    if hashed != user.first_name:
        return ('hacker')
    else:
        new_hash = hash(str(hashed))
        user.first_name = new_hash
        user.last_name = int(user.last_name) + int(i_price)
        user.save()

    # end update value


def sub_check(user, hashed, i_price):
    # update value
    if hashed != user.first_name:
        return ('hacker')
    if int(user.last_name) <= 0:
        return ('poor')
    else:
        new_hash = hash(str(hashed))
        user.first_name = new_hash
        value = int(user.last_name) - int(i_price)
        if value <= 0:
            return value
        user.last_name = value
        user.save()
        return value
    # end update value
# def reload(user, hashed, load, target):
#     #### add object that error when less than 0
#     if hashed != user.first_name:
#         return ('hacker')
#     new_hash = hash(str(hashed))
#     user.first_name = new_hash
#     user.last_name = int(user.last_name) - int(load)
#     user.save()
#     target.first_name = new_hash
#     target.last_name = int(target.last_name) + int(load)
#     target.save()
# def load(request):
#     if request.method == 'POST':
#         user = request.user
#         hashed = user.first_name
#         load = request.POST.get("load")
#         target = User.objects.get(username=request.POST.get("target"))
#         value = reload(user, hashed, load, target)
#         if value == 'hacker':
#             return HttpResponse('error')
#         return HttpResponse('reloaded the target')
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'commerce/sale/index.html', {
            'item': Item.objects.all().order_by('id').reverse(),
            'users': User.objects.all()
        })
    else:
        # if not request.user.is_authenticated:
        return render(request, "user/login.html")
        # return HttpResponseRedirect(reverse("user:login"))


def item(request, id):
    import datetime
    from datetime import date, time, datetime, timedelta

    # return render(request, 'commerce/sale/item.html')
    # return redirect('sale:index')
    orders = Order.objects.filter(user=request.user).order_by('id').reverse()
    item = Item.objects.get(id=id)
    ###############
    current_date = datetime.now()
    if item.expiration_date < current_date:
        item.notavailable = True
    else:
        item.notavailable = False
        #############
    return render(request, 'commerce/sale/item.html', {
        'orders': len(orders),
        'item': Item.objects.get(id=id),
        'ordered': Order.objects.filter(item=item)
    })


class Sale(forms.Form):

    cat = ('1', 'Service'), ('2', 'Goods')
    title = forms.CharField(required=True, label="Title")
    link = forms.CharField(required=True, label="link", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link'}))
    link2 = forms.CharField(required=False, label="link", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link (Optional)'}))
    link3 = forms.CharField(required=False, label="link2", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link (Optional)'}))
    link4 = forms.CharField(required=False, label="link3", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link (Optional)'}))
    link5 = forms.CharField(required=False, label="link4", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link (Optional)'}))
    link6 = forms.CharField(required=False, label="link5", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link (Optional)'}))
    link7 = forms.CharField(required=False, label="link6", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link (Optional)'}))
    link8 = forms.CharField(required=False, label="link7", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link (Optional)'}))
    link9 = forms.CharField(required=False, label="link8", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link (Optional)'}))
    link10 = forms.CharField(required=False, label="link9", widget=forms.TextInput(
        attrs={'placeholder': 'Picture Link (Optional)'}))
    price = forms.IntegerField(required=True)
    description = forms.CharField(
        required=True, label="Description", widget=forms.TextInput(attrs={'class': 'special'}))
    category = forms.ChoiceField(
        required=True, widget=forms.RadioSelect, choices=cat)
    paid = forms.IntegerField(required=True)


def create(request):
    from datetime import date, time, datetime, timedelta

    if request.method == 'POST':
        form = Sale(request.POST)
        if form.is_valid():
            value = int(form.cleaned_data["price"])
            list_d = datetime.now()
            paid_int = form.cleaned_data["paid"]
            paid_d = (timedelta(weeks=paid_int))
            o = Item(
                listing_date=list_d,
                paid_date=paid_int,
                expiration_date=list_d + paid_d,

                owner=request.user,
                link=form.cleaned_data["link"],
                link2=form.cleaned_data["link2"],
                link3=form.cleaned_data["link3"],
                link4=form.cleaned_data["link4"],
                link5=form.cleaned_data["link5"],
                link6=form.cleaned_data["link6"],
                link7=form.cleaned_data["link7"],
                link8=form.cleaned_data["link8"],
                link9=form.cleaned_data["link9"],
                link10=form.cleaned_data["link10"],
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                price=value,
                category=form.cleaned_data["category"]
            )

            # reduce the users' value
            v = request.user
            newValue = int(request.user.last_name) - value
            if newValue <= 0:
                return render(request, 'commerce/sale/create.html', {
                    # return redirect('sale:item', o.id)
                    'message': 'Please Reload Insufficient Balance',
                    'form': form
                })
            v.first_name = hash(str(newValue))
            v.last_name = newValue
            v.save()
            # save the listing
            o.save()
            return redirect('sale:item', o.id)
        else:
            return render(request, 'commerce/sale/create.html',
                          {
                              'form': form,
                              'message': 'form not valid'
                          })
    return render(request, 'commerce/sale/create.html', {
        'form': Sale()
    })
# class Update(forms.Form):
    # day = forms.IntegerField(required=True, label="Duration")


def update_create(request, id, csrf_token):

    if request.method == 'POST':
        update_day = int(request.POST.get('updated_day'))
        item = Item.objects.get(pk=id)
        add_date = int(item.paid_date) + int(update_day)
        item.paid_date = add_date
        item.expiration_date = item.expiration_date + \
            timedelta(weeks=update_day)
        ###############
        current_date = datetime.now()
        if item.expiration_date < current_date:
            item.notavailable = True
        else:
            item.notavailable = False
        #############
        item.save()
        return redirect('sale:mylist')
    return redirect('sale:mylist')


def order(request, item_id, hashed, i_price):
    if request.user.is_anonymous:
        return redirect('mail:login')
    user = request.user
    if request.method == 'GET':
        # item_id = request.GET['item_id']
        order = Item.objects.get(id=item_id)
        user = request.user
        owner = order.owner
        time = datetime.datetime.now()
        select = request.GET.get("select")
        qty = request.GET.get("qty")
        i_price2 = i_price * int(qty)
        if order.notavailable == False:
            if user in order.orders.all():
                # update value
                if add_check(user, hashed, i_price2) == 'hacker':
                    return HttpResponse('hacked')
                # end update value
                o = Order.objects.get(
                    i_id=order.id, user=user, item=order,  delivered=False)
                if o.delivered == True:
                    return HttpResponse('Fail to Unorder, Item already delivered')
                o.delete()
                order.orders.remove(user)

                return redirect('sale:item', item_id)
            else:
                # update value
                v = sub_check(user, hashed, i_price2)
                if v == 'hacker':
                    return HttpResponse('hacked')
                elif v == 'poor':
                    return HttpResponse('poor')
                elif v <= 0:
                    return HttpResponse('poor')
                # end update value
                o = Order.objects.create(i_total_price=i_price2, i_price=i_price, i_id=order.id,
                                         user=user, item=order, select=select, qty=qty, owner=order.owner, time=time)
                order.orders.add(user)
                order.save()

                return redirect('sale:myorder')
        else:
            return redirect('sale:item', item_id)
            # return HttpResponse('fail Already Delivered')
    # get user items
    elif request.method == 'POST':
        items = Item.objects.get(id=item_id)
        orders = Order.objects.filter(
            user=request.user).order_by('id').reverse()
        content = {
            'item': Item.objects.get(id=item_id),
            'ordered': Order.objects.all(),
            'orders': len(orders)
        }
    return redirect('sale:item', item_id)


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
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
        return HttpResponseRedirect(reverse("sale:index"))
    else:
        form = UserImageForm()
        return render(request, "commerce/sale/register.html",
                      {'form': form})


def register_view_alpha(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "commerce/sale/register.html", {
                "message": "Passwords must match"
            })
        try:
            user = User.objects.create_user(email, email, password)
            user.last_name = 1
            user.first_name = 1
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "commerce/sale/register.html", {
                "message":  "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("sale:index"))
    else:
        return render(request, "commerce/sale/register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("sale:index"))
        else:
            return render(request, "commerce/sale/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "commerce/sale/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("sale:login"))
