import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Name, Like, Follow, Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from datetime import datetime
import pytz
from django.http import JsonResponse
#user is lap
#profile is loaded
#name is mypigeong
from app_mail import models as mail


def following(request, username):
    if request.method == 'GET':
        w_u = get_object_or_404(mail.User, username=username)
        f = Profile.objects.filter(follower=w_u)
        f_p = Name.objects.all().order_by('id').reverse()
        p = []
        for ps in f_p:
            for fr in f:
                if fr.poster.username == ps.user:
                    p.append(ps)
        if not f:
            return render(request, 'a_social_network/following.html', {'d': "you dont follow anyone"})
        pgntr = Paginator(p, 10)
        pn = request.GET.get('page')
        pgobj = pgntr.get_page(pn)
        following_context = {
            "p": pgobj,
            's': "ss",
            "pd": f_p,
            "x": pgobj
        }
        return render(request, 'a_social_network/following.html', following_context)


############
@login_required
def postit(request):
    if request.method == "POST":
        ltz = pytz.timezone('Asia/Manila')
        now = datetime.now(ltz)
        dt = now.strftime("%A , %d %B %Y %X ")
        p = Name()
        p.user = request.user.username
        p.content = request.POST.get('content')
        p.timestamp = dt
        p.save()
        return redirect('social_network:index')
    else:
        return redirect('social_network:index')


###################


def upost(request, username):
    if request.method == 'GET':
        vng_u = request.user.username
        vng_u2 = request.user
        us = username
        vd_u = get_object_or_404(mail.User, username=username)
        p_o_u = Name.objects.filter(user=vd_u).order_by('id').reverse()

        nf = Name.objects.filter(user=vd_u)
        ####
        follower = Profile.objects.filter(poster=vd_u)
        following = Profile.objects.filter(follower=vd_u)
        #####
        if request.user.is_anonymous:
            return redirect('user:login')
        else:
            f_e_o = Profile.objects.filter(follower=vng_u2, poster=vd_u)
            totalfollower = len(follower)
            totalfollowing = len(following)

            pgntr = Paginator(p_o_u, 10)
            pn = request.GET.get('page')
            pgobj = pgntr.get_page(pn)

            return render(request, "a_social_network/users.html", {
                "xp": p_o_u,
                "pc": pgobj,
                "postuser": us,
                "uv":   vng_u,
                # "pagen":pagen,
                "vd": vd_u,
                "nf": nf,
                "x1": totalfollower,
                "x2": totalfollowing,
                "f": f_e_o,
            })
    else:
        vng_u = request.user.username
        vng_u2 = request.user
        vd_u = get_object_or_404(mail.User, username=username)
        p_o_u = Name.objects.filter(user=vd_u).order_by('id').reverse()
        us = username
        pgntr = Paginator(p_o_u, 10)
        pn = request.GET.get('page')
        pgobj = pgntr.get_page(pn)
        nf = Name.objects.filter(user=vd_u)
        f_e_o = Profile.objects.filter(follower=vng_u2, poster=vd_u)
        if not f_e_o:
            fo = Profile.objects.create(poster=vd_u, follower=vng_u2)
            fo.save()
            follower = Profile.objects.filter(follower=vng_u2, poster=vd_u)
            following = Profile.objects.filter(follower=vd_u)
            f_e_o = Profile.objects.filter(follower=vng_u2, poster=vd_u)
            totalfollower = len(follower)
            totalfollowing = len(following)
            inside = {
                "xp": p_o_u,
                "pc": pgobj,
                "postuser": us,
                "uv":   vng_u,
                "vd": vd_u,
                "nf": nf,
                "x1": totalfollower,
                "x2": totalfollowing,
                "f":    f_e_o,
            }
            return render(request, "a_social_network/users.html", inside)
        else:
            f_e_o.delete()
            ##
            follower = Profile.objects.filter(poster=vd_u)
            following = Profile.objects.filter(follower=vd_u)
            totalfollower = len(follower)
            totalfollowing = len(following)
            inside = {
                "xp": p_o_u,
                "pc": pgobj,
                "postuser": us,
                "uv":   vng_u,
                # "pagen": pagen,
                "vd": vd_u,
                "nf": nf,

                "x1": totalfollower,
                "x2": totalfollowing,
                "f":    f_e_o
            }
            return render(request, "a_social_network/users.html", inside)


def like_post(request):
    user = request.user
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id)

        if user in likedpost.liked.all():
            likedpost.liked.remove(user)
            like = Like.objects.get(post=likedpost, user=user)
            like.delete()
        else:
            like = Like.objects.get_or_create(post=likedpost, user=user)
            likedpost.liked.add(user)
            likedpost.save()
        return HttpResponse('Success')

###################

    # return to the same page
 # return redirect(request.META['HTTP_REFERER'])


##############


@csrf_exempt
def like(request, post_id):
    likedpost = Name.objects.get(pk=post_id)
    if request.method == 'POST':
        user = request.user
        if user in likedpost.likes.all():
            likedpost.likes.remove(user)
            like = Like.objects.get(post=likedpost, user=user)
            like.delete()
        else:
            like = Like.objects.get_or_create(post=likedpost, user=user)
            likedpost.likes.add(user)
            likedpost.save()
        return redirect(request.META['HTTP_REFERER'])
        return JsonResponse([likedposts.serialize() for likedposts in likedpost], safe=False)
####################


def delete(request, post_id):
    post = Name.objects.get(pk=post_id)
    if request.method == 'POST':
        post.delete()
        payload = {'success': True}
        return redirect(request.META['HTTP_REFERER'])


###################


@csrf_exempt
def edit(request, post_id):
    if request.method == 'POST':
        post = Name.objects.get(pk=post_id)

        data = json.loads(request.body)
        x = data.get("c")

    #    textarea = request.POST["textarea"]
        post.content = x
        post.save()
        return redirect(request.META['HTTP_REFERER'])

###################
###################


def index(request):
    posts = Name.objects.all().order_by('id').reverse()
    vuser = request.user.username
    xuser = request.user
    # posts = Post.objects.all()  # Getting all the posts from database
    # return render(request, 'post/index.html', { 'posts': posts })
    pgntr = Paginator(posts, 10)
    pn = request.GET.get('page')
    pgobj = pgntr.get_page(pn)

    return render(request, "a_social_network/index.html", {
        "posts": pgobj,
        # "puser": pmail.user,
        "vuser": vuser,
        "xuser": xuser
    })


def index2(request):
    posts = Name.objects.all()
    vuser = request.user.username
    xuser = request.user
    # posts = Post.objects.all()  # Getting all the posts from database
    # return render(request, 'post/index.html', { 'posts': posts })
    pgntr = Paginator(posts, 10)
    pn = request.GET.get('page')
    pgobj = pgntr.get_page(pn)
    xp = posts.order_by('id').reverse()
    return JsonResponse([post.serialize() for post in pgobj], safe=False)

    # return render(request, "a_social_network/index.html" , {
    #    "posts":pgobj,
    #    "vuser": vmail.user,
    #    "xuser" : xuser
    # })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("social_network:index"))
        else:
            return render(request, "a_social_network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "a_social_network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("social_network:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "a_social_network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "a_social_network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("social_network:index"))
    else:
        return render(request, "a_social_network/register.html")
