from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from app_mail.models import User
from django.urls import reverse

# Create your views here.
def commerce(request):
    return render(request, 'commerce/commerce.html')
def auction(request):
    return render(request, 'commerce/auction/index.html')
def sale(request):
    return redirect('sale:index')


def load(request):
    if request.method == 'POST':
        user = request.user
        hashed = user.first_name
        load = request.POST.get("load")
        target = User.objects.get(username=request.POST.get("target"))
        value = reload(user, hashed, load, target)
        if value == 'hacker':
            return HttpResponse('error')
        return HttpResponseRedirect(reverse("commerce:commerce"))
    return HttpResponseRedirect(reverse("commerce:commerce"))
def reload(user, hashed, load, target):
    #### add object that error when less than 0
    if hashed != user.first_name:
        return ('hacker')
    new_hash = hash(str(hashed))
    user.first_name = new_hash
    new_load = int(user.last_name) - int(load)
    ## added
    if new_load <= 0:
        return HttpResponse("poor")
        ##
    user.last_name = new_load
    user.save()
    target.first_name = new_hash
    target.last_name = int(target.last_name) + int(load)
    target.save()