from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from app_mail.models import User
from django.urls import reverse
from user import transactions
from django.http import JsonResponse

# Create your views here.


def commerce(request):

    return render(request, 'commerce/commerce.html')


def auction(request):
    return render(request, 'commerce/auction/index.html')


def sale(request):
    return redirect('sale:index')


def load(request):
    if request.method == 'POST':

        hashed = request.POST.get("hashed")

        transactions.load(request)
        return redirect("user:userpage")
    return redirect("user:userpage")


def reload(user, hashed, load, target):
    # add object that error when less than 0
    transactions.reload(user, hashed, load, target)
