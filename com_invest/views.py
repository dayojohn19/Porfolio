from datetime import datetime
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from .models import Investor, Total_Investment, InvestmentRecord


def index(request):
    return render(request, 'commerce/invest/index.html')


def about(request):
    return render(request, 'commerce/invest/about.html')


def table(request):
    #  /////// AUTHENTICATE USER ? //////
    # if request.user.is_authenticated:
    #     return redirect('invest:index')
    try:
        investors = Investor.objects.all().order_by('-invested_percentage')
        investments = Total_Investment.objects.get(stock='php')

        records = InvestmentRecord.objects.all().order_by('-id')
        return render(request, 'commerce/invest/table.html', {
            'investors': investors,
            'investments': investments,
            'invest_records': records
        })
    except:
        return render(request, 'commerce/invest/table.html', {

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
            return redirect('invest:table')
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


def portfolio(request):
    return render(request, 'commerce/invest/portfolio.html')


def reinvest(request, csrf_token):
    if request.method == 'POST':
        try:

            amount = request.POST.get('amount')
            amount = int(amount)
            investor_id = request.POST.get('investor_id')
            # calculating the investor
            investor = Investor.objects.get(id=investor_id)
            stock = 'php'
            try:
                invest = Total_Investment.objects.get(stock=stock)
            except:
                invest = Total_Investment.objects.create(
                    amount=0, average=0, stock=stock)

            invest.amount += float(amount)
            invest.quantity = invest.amount
            invest.average = float(invest.amount) / float(invest.quantity)
            invest.save()

            investor.invested_amount += amount

            investor.invested_percentage = float(
                investor.invested_amount) / float(invest.amount) * 100

            investor.reinvested = datetime.now()
            print('Trying... \n\n')
            investor.save()
            # recording the investment
            new_invest = InvestmentRecord()
            new_invest.invest_amount = amount
            new_invest.investor_name = investor.investor_name

            new_invest.invesotr_id = investor_id
            new_invest.save()
            return redirect('invest:table')
        except:
            print('\n CAnt find the user')
            return redirect('invest:table')

    return redirect('invest:table')
