from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls.conf import path
from .models import Bid,Listing,Comment,Watchlist,Closedbid,Alllisting
from datetime import datetime

from django.shortcuts import render
from .forms import ImageForm
from app_mail.models import User
def math(request):
    return render(request, "auction/math.html")
def create(request):
    try:
        w = Watchlist.objects.filter(user=request.user.username)
        wcount=len(w)
        form = ImageForm(request.POST, request.FILES)
        form2 = ImageForm(use_required_attribute=False)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'auction/create.html', {'form': form, 'img_obj': img_obj})
    except:
        wcount=None
    return render(request,"auction/create.html",{
        "wcount":wcount,
        'form': form2
    })


def index(request):
    
    items=Listing.objects.all()
    try:
        w = Watchlist.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request, "auction/index.html",{
        "items":items,
        "wcount":wcount
    })

def categories(request):
    # items=Listing.objects.raw("SELECT * FROM auction_listing GROUP BY category")
    items=Listing.objects.all()
    try:
        w = Watchlist.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"auction/categpage.html",{
        "items": items,
        "wcount":wcount
    })

def category(request,category):
    catitems = Listing.objects.filter(category=category)
    try:
        w = Watchlist.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"auction/category.html",{
        "items":catitems,
        "cat":category,
        "wcount":wcount
    })

import pytz
def submit(request):
    if request.method == "POST":
        listtable = Listing()
        ltz = pytz.timezone('Asia/Manila')
        now = datetime.now(ltz)
        dt = now.strftime("%A %d %B %Y %X ")

        listtable.owner = request.user.username
        listtable.title = request.POST.get('title')
        listtable.description = request.POST.get('description')
        listtable.price = request.POST.get('price')
        listtable.category = request.POST.get('category')
        if request.POST.get('link'):
            listtable.link = request.POST.get('link')
        else :
            listtable.link = "https://nas-national-prod.s3.amazonaws.com/styles/hero_image/s3/_web_apa_2016_rock-pigeon_laura_perrotta_kk.jpg?itok=JbOQMi8b"
        listtable.time = dt
        listtable.save()
        all = Alllisting()
        items = Listing.objects.all()


        for i in items:
            try:
                if Alllisting.objects.get(listingid=i.id):
                    pass
            except:
                all.listingid=i.id
                all.title = i.title
                all.description = i.description
                all.link = i.link
                all.save()

        return redirect('auction:index')
    else:
        return redirect('auction:index')

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'auction/create.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'auction/create.html', {'form': form})
    ##############



def listingpage(request,id):
    try:
        item = Listing.objects.get(id=id)
    except:
        return redirect('auction:index')
    try:
        comments = Comment.objects.filter(listingid=id)
    except:
        comments = None
    if request.user.username:
        try:
            if Watchlist.objects.get(user=request.user.username,listingid=id):
                added=True
        except:
            added = False
        try:
            l = Listing.objects.get(id=id)
            if l.owner == request.user.username :
                owner=True
            else:
                owner=False
        except:
            return redirect('auction:index')
    else:
        added=False
        owner=False
    try:
        w = Watchlist.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"auction/listingpage.html",{
        "i":item,
        "error":request.COOKIES.get('error'),
        "errorgreen":request.COOKIES.get('errorgreen'),
        "comments":comments,
        "added":added,
        "owner":owner,
        "wcount":wcount
    })

def bidsubmit(request,listingid):
    current_bid = Listing.objects.get(id=listingid)
    current_bid=current_bid.price
    if request.method == "POST":
        user_bid = int(request.POST.get("bid"))
        if user_bid > current_bid:
            user = User.objects.get(pk=request.user.id)
            user.last_name = int(user_bid) - int(user.last_name)
            if user.last_name <=  0:
                return
            listing_items = Listing.objects.get(id=listingid)
            listing_items.price = user_bid
            listing_items.save()

            user.save()

            try:
                if Bid.objects.filter(id=listingid):
                    bidrow = Bid.objects.filter(id=listingid)
                    bidrow.delete()
                bidtable = Bid()
                bidtable.user=request.user.username
                bidtable.title = listing_items.title
                bidtable.listingid = listingid
                bidtable.bid = user_bid
                bidtable.save()
                
            except:
                bidtable = Bid()
                bidtable.user=request.user.username
                bidtable.title = listing_items.title
                bidtable.listingid = listingid
                bidtable.bid = user_bid
                bidtable.save()
            response = redirect('auction:listingpage',id=listingid)
            response.set_cookie('errorgreen','bid successful!!!',max_age=3)
            return response
        else :
            response = redirect('auction:listingpage',id=listingid)
            response.set_cookie('error','Bid should be greater than  Highest Bid',max_age=3)
            return response
    else:
        return redirect('auction:index')


def cmntsubmit(request,listingid):
    if request.method == "POST":
        ltz = pytz.timezone('Asia/Manila')
        now = datetime.now(ltz)
        dt = now.strftime("%AC %d %B %Y %X ")
        c = Comment()
        c.comment = request.POST.get('comment')
        c.user = request.user.username
        c.time = dt
        c.listingid = listingid
        c.save()
        return redirect('auction:listingpage',id=listingid)
    else :
        return redirect('auction:index')

def addwatchlist(request,listingid):
    if request.user.username:
        w = Watchlist()
        w.user = request.user.username
        w.listingid = listingid
        w.save()
        return redirect('auction:listingpage',id=listingid)
    else:
        return redirect('auction:index')


def removewatchlist(request,listingid):
    if request.user.username:
        try:
            w = Watchlist.objects.get(user=request.user.username,listingid=listingid)
            w.delete()
            return redirect('auction:listingpage',id=listingid)
        except:
            return redirect('auction:listingpage',id=listingid)
    else:
        return redirect('auction:index')

def watchlistpage(request,username):
    if request.user.username:
        try:
            w = Watchlist.objects.filter(user=username)
            items = []
            for i in w:
                items.append(Listing.objects.filter(id=i.listingid))
            try:
                w = Watchlist.objects.filter(user=request.user.username)
                wcount=len(w)
            except:
                wcount=None
            return render(request,"auction/watchlistpage.html",{
                "items":items,
                "wcount":wcount
            })
        except:
            try:
                w = Watchlist.objects.filter(user=request.user.username)
                wcount=len(w)
            except:
                wcount=None
            return render(request,"auction/watchlistpage.html",{
                "items":None,
                "wcount":wcount
            })
    else:
        return redirect('auction:index')

def closebid(request,listingid):
    if request.user.username:
        try:
            listingrow = Listing.objects.get(id=listingid)
        except:
            return redirect('auction:index')
        cb = Closedbid()
        title = listingrow.title
        cb.owner = listingrow.owner
        cb.listingid = listingid
        try:
            bidrow = Bid.objects.get(listingid=listingid,bid=listingrow.price)
            cb.winner = bidrow.user
            cb.winprice = bidrow.bid
            cb.save()
            bidrow.delete()
        except:
            cb.winner = listingrow.owner
            cb.winprice = listingrow.price
            cb.save()
        try:
            if Watchlist.objects.filter(listingid=listingid):
                watchrow = Watchlist.objects.filter(listingid=listingid)
                watchrow.delete()
            else:
                pass
        except:
            pass
        try:
            crow = Comment.objects.filter(listingid=listingid)
            crow.delete()
        except:
            pass
        try:
            brow = Bid.objects.filter(listingid=listingid)
            brow.delete()
        except:
            pass
        try:
            cblist=Closedbid.objects.get(listingid=listingid)
        except:
            cb.owner = listingrow.owner
            cb.winner = listingrow.owner
            cb.listingid = listingid
            cb.winprice = listingrow.price
            cb.save()
            cblist=Closedbid.objects.get(listingid=listingid)
        listingrow.delete()
        try:
            w = Watchlist.objects.filter(user=request.user.username)
            wcount=len(w)
        except:
            wcount=None
        return render(request,"auction/winningpage.html",{
            "cb":cblist,
            "title":title,
            "wcount":wcount
        })   

    else:
        return redirect('auction:index')     

def mywinnings(request):
    if request.user.username:
        items=[]
        try:
            wonitems = Closedbid.objects.filter(winner=request.user.username)
            for w in wonitems:
                items.append(Alllisting.objects.filter(listingid=w.listingid))
        except:
            wonitems = None
            items = None
        try:
            w = Watchlist.objects.filter(user=request.user.username)
            wcount=len(w)
        except:
            wcount=None
        return render(request,'auction/mywinnings.html',{
            "items":items,
            "wcount":wcount,
            "wonitems":wonitems
        })
    else:
        return redirect('auction:index')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auction:index"))
        else:
            return render(request, "auction/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auction/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auction:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auction:index"))
    else:
        return render(request, "auctions/register.html")
