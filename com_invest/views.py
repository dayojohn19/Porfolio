from datetime import datetime
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from .models import Investor, Total_Investment


def index(request):
    return render(request, 'commerce/invest/index.html')


def table(request):
    #  /////// AUTHENTICATE USER ? //////
    # if request.user.is_authenticated:
    #     return redirect('invest:index')
    investors = Investor.objects.all().order_by('-invested_percentage')
    investments = Total_Investment.objects.get(stock='php')
    return render(request, 'commerce/invest/table.html', {
        'investors': investors,
        'investments': investments
    })


def add_investor(request, csrf_token):
    if request.method == 'POST':
        # item_id = request.POST.get("item_id")
        investor_name = request.POST.get('investor_name')
        investment_amount = request.POST.get('investment_amount')
        investor_contact = request.POST.get('contact')

        try:
            stock = request.POST.get('stock_name')
        except:
            stock = 'php'
        stock = 'php'
        try:
            investor = Investor.objects.get(investor_name=investor_name)
        except:
            investor = Investor.objects.create(
                investor_name=investor_name, investor_contact=investor_contact, invested_amount=0, invested_percentage=0, reinvested=datetime.now()
            )
        try:
            invest = Total_Investment.objects.get(stock=stock)
        except:
            invest = Total_Investment.objects.create(
                amount=0, average=0, stock=stock)

        invest.amount += float(investment_amount)
        invest.quantity = invest.amount
        invest.average = float(invest.amount) / float(invest.quantity)
        invest.save()

        investor.invested_amount += float(investment_amount)
        investor.invested_percentage = float(investor.invested_amount) / float(
            invest.amount) * 100

        investor.reinvested = datetime.now()
        investor.save()
        # update all the investor's percentage
        all_investors = Investor.objects.all()
        for all_investor in all_investors:
            all_investor.invested_percentage = (
                float(all_investor.invested_amount) / float(invest.amount)) * 100
            all_investor.save()

    return redirect('invest:table')

    # return render(request, 'commerce/invest/table.html')


def reports(request):
    return render(request, 'commerce/invest/reports.html')
