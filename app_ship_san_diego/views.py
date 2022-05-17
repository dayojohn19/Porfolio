from .models import MySanDiegoDays, Comment
from django.shortcuts import render
from .forms import DaysForm
# Create your views here.
from .forms import DaysForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect



def index(request):
    return render(request, 'app_san_diego/index.html')
    # return HttpResponseRedirect(reverse("ship_san_diego:read"))


def newPost(request):
    if request.method == 'POST':
        form = DaysForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'app_san_diego/post.html', {'daysForm': img_obj})
        else:
            print('NOT VALID')
    else:
        form = DaysForm()

    return render(request, 'app_san_diego/post.html', {'daysForm': form})


def editPost(request):
    from .models import MySanDiegoDays
    from app_mail.models import User
    if request.method == 'POST':
        try:
            if (request.POST.get('title') != ''):
                post.title = request.POST.get('title')
        except:
            pass
        try:
            if (request.POST.get('feeling') != ''):
                post.feeling = request.POST.get('feeling')
        except:
            pass
        try:
            if (request.POST.get('country') != ''):
                post.country = request.POST.get('country')
        except:
            pass

        post_id = request.POST.get('id')
        post = MySanDiegoDays.objects.get(id=post_id)
        post.poster_id = request.POST.get('poster_id')
        post.poster = User.objects.get(pk=post.poster_id).username
        post.courseTrue = request.POST.get('course')
        post.activity = request.POST.get('activity')
        post.latitude = request.POST.get('latitude')
        post.longitude = request.POST.get('longitude')

        post.vicinity = request.POST.get('vicinity')
        post.speed = request.POST.get('speed')
        post.DutiesAndEvents = request.POST.get('dutiesandevents')

        post.save()


def readPost(request):

    items = MySanDiegoDays.objects.all().order_by('id').reverse()
    return render(request, 'app_san_diego/read.html', {'items': items})


def gallery(request):
    items = MySanDiegoDays.objects.all().order_by('id').reverse()
    return render(request, 'app_san_diego/gallery.html', {'items': items})


def comment(request, id):
    pass
    if request.method == 'POST':
        try:
            post = MySanDiegoDays.objects.get(pk=id)
            new_comment = Comment()
            try:
                new_comment.user = request.user.username
            except:
                new_comment.user = 'Anonymous'
            try:
                new_comment.user_picture = request.user.email
            except:
                pass
            new_comment.contact = request.POST['user_contact']
            new_comment.say = request.POST["user_comment"]
            new_comment.save()
            post.comments.add(new_comment)
            print('DONE \n\n')
        except:
            print('not Done \n\n')
    return redirect('ship_san_diego:view', id)

    # return HttpResponseRedirect('ship_san_diego:view', id)


def view(request, id):
    try:
        items = MySanDiegoDays.objects.get(id=id)
        return render(request, 'app_san_diego/gallery.html', {'items': items, 'solo': 'solo'})
    except:
        items = MySanDiegoDays.objects.filter(poster_id=id)
        return render(request, 'app_san_diego/gallery.html', {'items': items, 'solo': 'solo'})
