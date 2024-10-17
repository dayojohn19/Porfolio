from datetime import datetime
from django.shortcuts import render
import math
# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from .models import Investor, Total_Investment, InvestmentRecord, StocksHand, TradeRecords, SideComputations, DividendRecord, InterestTypes


def index(request):
    return render(request, 'commerce/invest/index.html')


def contact(request, userMessage):
    context = {
        'userMessage': userMessage
    }
    return render(request, 'commerce/invest/contact.html', context)


# def computations(request):
#     return render(request, 'commerce/invest/computations.html')

def RecordTotalTransactionCost(side, stockName, stockQuantity, stockPrice, transactionAmount):

    newTransactionAfterTax = TradeRecords.objects.create(stockQuantity=stockQuantity,
                                                         TransactionSide=side, stockName=stockName, stockPrice=stockPrice, CostAfterTax=transactionAmount)
    newTransactionAfterTax.save()
    YearToday = 2022  # Change this to year today
    try:
        sideCompute = SideComputations.objects.get(
            YearComputation=YearToday, side=side)
    except:
        sideCompute = SideComputations.objects.create(
            YearComputation=YearToday, side=side)
        sideCompute.save()

    sideCompute.sideAmount += transactionAmount
    sideCompute.save()
    # DONE RECORD +++++++

    OverAllInvestmentAmount = Total_Investment.objects.get(
        stock='php')
    if side == 'buy':
        if OverAllInvestmentAmount.balance < transactionAmount:
            return redirect('invest:portfolio')
        OverAllInvestmentAmount.balance -= transactionAmount
        OverAllInvestmentAmount.portfolioValue += transactionAmount
        OverAllInvestmentAmount.save()

    # SIDE INTEREST COMPUTATION
    try:
        print('MAKING PROFIT..')
        SellSideAmount = SideComputations.objects.get(
            side='sell', YearComputation=YearToday)
        BuySideAmount = SideComputations.objects.get(
            side='buy', YearComputation=YearToday)

        print('MAKING PROFIT SELL...', SellSideAmount.sideAmount)
        sideProfit = int(SellSideAmount.sideAmount) - \
            int(BuySideAmount.sideAmount)
        print('MAKING PROFIT BUY ....', BuySideAmount.sideAmount)

        # calculate percentage Interest before adding the profit to the iclub Value
        if side == 'sell':
            OverAllInvestmentAmount.amount = sideProfit + \
                OverAllInvestmentAmount.gatheredAmount
            OverAllInvestmentAmount.portfolioValue -= transactionAmount
            OverAllInvestmentAmount.save()

            OverAllInvestmentAmount.balance += transactionAmount
            UpdateInvestorsValue(0)
            # OverAllInvestmentAmount.balance = OverAllInvestmentAmount.amount

        sideInterest = (
            sideProfit / OverAllInvestmentAmount.gatheredAmount)*100
        print('MAKING PROFIT')
        try:

            ProfitSideAmount = SideComputations.objects.get(
                side='profit')
        except:
            ProfitSideAmount = SideComputations()
            ProfitSideAmount.side = 'profit'

        ProfitSideAmount.InterestComputation = sideInterest
        ProfitSideAmount.ProfitComputation = sideProfit

        OverAllInvestmentAmount.save()
        ProfitSideAmount.save()
    except:
        print('\n\n\n\n FAIL GET PROFIT AND iNTEREST ')
        pass

    print('\n\n\n SAVED')
    return


def HandoutStock(request):
    if request.method != 'POST':
        return redirect('invest:portfolio')
    stockNameNew = request.POST.get('stockName')
    stockSellPrice = float(request.POST.get('SellStockPrice'))
    #
    stockQuantity = float(request.POST.get('stockQuantitySell'))
    totalSellCostAfterTax = int(request.POST.get('totalSellCost2'))
    print('\n\n\n\n COST AFTER TAX', totalSellCostAfterTax)
    try:

        stockItem = StocksHand.objects.get(stockName=stockNameNew)
        if (stockQuantity > stockItem.stockQuantity):
            return
        stockItem.stockQuantity -= stockQuantity
        if stockItem.stockQuantity <= 0:
            stockItem.delete()
        else:
            stockItem.save()
    # RECORDING TRANSACTION AFTER TAX COST
        RecordTotalTransactionCost('sell', stockNameNew, stockQuantity,
                                   stockSellPrice, totalSellCostAfterTax)
    except:

        pass
    return redirect('invest:portfolio')


def HandinStock(request):
    if request.method != 'POST':
        return redirect('invest:portfolio')
    stockNameNew = request.POST.get('stockName')
    stockQuantityNew = float(request.POST.get('stockQuantity'))
    stockBuyPriceNew = float(request.POST.get('stockBuyPrice'))
    stockCost2 = float(stockBuyPriceNew) * float(stockQuantityNew)
    if (stockCost2 > Total_Investment.objects.get(stock='php').balance):
        return redirect('invest:portfolio')
    try:
        stockItem = StocksHand.objects.get(stockName=stockNameNew)
        stockCost1 = float(stockItem.stockBuyPrice) * \
            float(stockItem.stockQuantity)

        stockCost = stockCost1 + stockCost2

        stockItem.stockQuantity = int(
            stockQuantityNew) + int(stockItem.stockQuantity)

        # priceStock = int(stockItem.stockBuyPrice) + int(stockBuyPriceNew)

        # stockItem.stockBuyPrice = float(stockCost) / stockItem.stockQuantity
        stockItem.stockBuyPrice = round(
            float(stockCost) / stockItem.stockQuantity, 3)

        stockItem.save()
    except:
        stockItem = StocksHand.objects.create(
            stockQuantity=stockQuantityNew, stockBuyPrice=stockBuyPriceNew, stockName=stockNameNew)
    # RECORDING TRANSACTION AFTER TAX COST
    totalBuyCostAfterTax = int(request.POST.get('totalBuyCostAfterTax'))
    RecordTotalTransactionCost('buy', stockNameNew, stockQuantityNew,
                               stockBuyPriceNew, totalBuyCostAfterTax)
    #
    return redirect('invest:portfolio')


def InvestAmount(request, csrf_token):  # INVEST AMOUNT IS PROFIT AMOUNT
    if request.method == 'POST':
        investAmount = int(request.POST.get('InvestAmount'))
        UpdateInvestorsValue(investAmount)

        EditediClubValue = TradeRecords.objects.create(stockQuantity=0,
                                                       TransactionSide='calculated', stockName='in_hand', stockPrice=0, CostAfterTax=investAmount)
        EditediClubValue.save()
    # investItem = Total_Investment.objects.get(stock='php')###
    # investBalance = int(investItem.amount)###
    # print('\n\n\n THIS INVESTMENT: ', investBalance)
    # investItem.amount += investAmount###
    # investItem.save()###
    #
    # AllInvestors = Investor.objects.all()
    # UpdateAllInvestorPercentage()
    # for eachInvestor in AllInvestors:
    #     eachInvestor.invested_value += (
    #         eachInvestor.invested_percentage / 100) * investAmount
    #     eachInvestor.save()
    print('\n\n DONE UPDATING INVESTED VALUE')
    return redirect('invest:records')


def UpdateInvestorsValue(added_ClubValue):
    investItem = Total_Investment.objects.get(stock='php')
    investBalance = int(investItem.amount)
    # investItem.amount += investAmount
    investItem.amount += added_ClubValue
    investItem.balance += added_ClubValue
    investItem.save()
    AllInvestors = Investor.objects.all()
    for eachInvestor in AllInvestors:
        # eachInvestor.invested_value += (
        eachInvestor.invested_value = (
            # eachInvestor.invested_percentage / 100) * investAmount
            eachInvestor.invested_percentage / 100) * investItem.amount
        eachInvestor.save()


def options(request):
    return render(request, 'commerce/invest/options.html')


def records(request):
    #  /////// AUTHENTICATE USER ? //////
    # if request.user.is_authenticated:
    #     return redirect('invest:index')
    # try:

    investmentRecords = InvestmentRecord.objects.all().order_by('-id')
    dividendsRecords = DividendRecord.objects.all().order_by('-id')
    tradeRecords = TradeRecords.objects.all().order_by('-id')

    return render(request, 'commerce/invest/records.html', {

        'investmentRecords': investmentRecords,
        'dividendsRecords': dividendsRecords,
        'tradeRecords': tradeRecords
    })
    # except:
    #     return render(request, 'commerce/invest/records.html', {

    #     })


def add_investor(request, csrf_token):
    if request.method == 'POST':
        # item_id = request.POST.get("item_id")
        investor_name = request.POST.get('investor_name')
        investment_amount = request.POST.get('investment_amount')
        investor_contact = request.POST.get('contact')

        # investorContract = InterestTypes.objects.create(type=request.POST.get('interestType'), percentage=request.POST.get(
        #     'interestPercentage'), duration=request.POST.get('interestDuration'))
        try:
            stock = request.POST.get('stock_name')
        except:
            stock = 'php'
        stock = 'php'
        try:
            print('\n\n\n Trying.NAME: ', investor_name)
            investor = Investor.objects.get(investor_name=investor_name)
            # return already exists name
            return redirect('invest:records')
        except:
            print('\n\n\n Trying..')
            investor = Investor.objects.create(
                investor_name=investor_name, investor_contact=investor_contact, invested_amount=0, invested_percentage=0, reinvested=datetime.now()
            )
        try:
            print('\n\n\n Trying...')
            invest = Total_Investment.objects.get(stock=stock)
        except:
            print('\n\n\n Trying....')
            invest = Total_Investment.objects.create(
                amount=0, gatheredAmount=0, stock=stock)
        iClubTotalValue = invest.amount

        invest.amount += float(investment_amount)
        invest.balance += int(investment_amount)
        invest.quantity = invest.amount
        invest.gatheredAmount += float(investment_amount)
        invest.save()

        # should be first before updating value
        InvestmentValue = investor.invested_value
        investor.invested_amount += float(investment_amount)
        investor.invested_value += investor.invested_amount
        investor.reinvested = datetime.now()

        # ----- INTEREST CONTRACT
        investor.interest = float(request.POST.get('interestPercentage'))
        investor.duration = request.POST.get('interestDuration')
        interestType = request.POST.get('interestType')
        investor.interestType = interestType
        investor.save()
        try:
            TypeOfInterest = InterestTypes.objects.get(Year=2022)
        except:
            TypeOfInterest = InterestTypes.objects.create(Year=2022)
        if interestType == 'ratio':
            TypeOfInterest.RatioInterest.add(investor)
        elif interestType == 'fix':
            TypeOfInterest.FixInterest.add(investor)
        elif interestType == 'growth':
            # TypeOfInterest.GrowthInterest.add(investor)
            TypeOfInterest.GrowthInterest.add(investor)

        TypeOfInterest.save()
        # -----

        #  BELOW LINE CAN BE CHANGED TO UpdateAllInvestorPercentage()
        UpdateAllInvestorPercentage()
        # investor.invested_percentage = float(investor.invested_amount) / float(
        #     invest.amount) * 100

        #
        InvestmentAmount = investor.invested_amount
        investor_id = investor.id
        investor_Name = investor.investor_name
        percentage_before = investor.invested_percentage
        percentage_after = investor.invested_percentage
        recordInvestment(iClubTotalValue, InvestmentAmount, InvestmentValue, investor_id,
                         investor_Name, percentage_before, percentage_after)
        #  -------------
        # UpdateAllInvestorPercentage()
        # update all the investor's percentage
        # all_investors = Investor.objects.all()
        # for all_investor in all_investors:
        #     all_investor.invested_percentage = (
        #         float(all_investor.invested_amount) / float(invest.amount)) * 100
        #     all_investor.save()

    return redirect('invest:records')


def UpdateAllInvestorPercentage():
    print('\n\n UPDATING \n')
    stock = 'php'
    try:
        invest = Total_Investment.objects.get(stock=stock)
    except:
        invest = Total_Investment.objects.create(
            amount=0, gatheredAmount=0, stock=stock)
    all_investors = Investor.objects.all()
    for all_investor in all_investors:
        all_investor.invested_percentage = round(
            ((float(all_investor.invested_value) / float(invest.amount)) * 100), 3)
        all_investor.save()


def portfolio(request):
    try:
        stocksInHand = StocksHand.objects.all()
        TotalInvestment = Total_Investment.objects.get(stock='php')
    except:
        return redirect('invest:records')
    try:
        TotalSold = SideComputations.objects.get(side='sell').sideAmount
        TotalProfit = SideComputations.objects.get(
            side='profit')
    except:
        TotalSold = 'None'
        TotalProfit = 'None'
    try:
        TotalBought = SideComputations.objects.get(side='buy').sideAmount
    except:
        TotalBought = 'None'
    try:
        investments = Total_Investment.objects.get(stock='php')
    except:
        investments = Total_Investment.objects.create(stock='php')
    investors = Investor.objects.all().order_by('-invested_percentage')
    contexts = {
        'stocksInHand': stocksInHand,
        'investors': investors,
        'TotalSold': TotalSold,
        'TotalBought': TotalBought,
        'TotalProfit': TotalProfit,
        'investments': investments,
        'TotalInvestment': TotalInvestment,
    }
    return render(request, 'commerce/invest/portfolio.html', contexts)


def checkMyRecord(request, investor_id):
    print('\n\n\n\n ', investor_id)
    try:
        investor_record = InvestmentRecord.objects.filter(
            investor_id=investor_id).order_by('-id')
        investor_profile = Investor.objects.get(pk=investor_id)
        context = {
            'my_record': investor_record,
            'investor_profile': investor_profile
        }
    except:
        context = {
            'message': 'Record Cant be Found'
        }

    return render(request, 'commerce/invest/personalRecord.html', context)


def recordInvestment(iClubTotalValue, InvestmentAmount, InvestmentValue, investor_id, investor_Name, percentage_before, percentage_after):
    print('INVESTING...')
    new_invest = InvestmentRecord()
    new_invest.invest_amount = InvestmentAmount  # InvestedAmount
    new_invest.investor_name = investor_Name
    print('INVESTING...')
    #
    new_invest.investedPercentageBefore = percentage_before
    # New Investment Percentage after new Investment
    new_invest.investedPercentageAfter = percentage_after
    # total iClubValue at the Time of Investment
    new_invest.CurrentiClubValue = iClubTotalValue
    new_invest.invest_valueBefore = InvestmentValue
    print('INVESTING...')
    #
    new_invest.investor_id = investor_id
    new_invest.save()
    pass


def reinvest(request, csrf_token):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        amount = int(amount)
        investor_id = request.POST.get('investor_id')
        # calculating the investor
        reinvestFunction(investor_id, amount)
    return redirect('invest:records')


def reInvestLowerThanInvestedAmount(investor_ID):
    pass
    # Get investor_ID
    # lowerAmount = invested_amount that is lower than 0
    # Profit = after Share Value was deducted From all total Invested Amount
    # RATIO =  CONTRACT PERCENTAGE divide Profit
    # Withdrawable Amount = (Contract /100) * Profit
    # TotallowerAmount = (lowerAmount * Ration )
    # Then subtract TotallowerAmount to (Remaining Share Value or Profit ):


def reinvestFunction(investor_id, amount):
    try:
        investor = Investor.objects.get(id=investor_id)
        stock = 'php'
        try:
            invest = Total_Investment.objects.get(stock=stock)
        except:
            invest = Total_Investment.objects.create(
                amount=0, gatheredAmount=0, stock=stock)

        InvestmentAmount = amount

        investor_Name = investor.investor_name

        percentage_before = investor.invested_percentage
        iClubTotalValue = invest.amount
        # ADDING VALUE TO ICLUB
        invest.amount += float(amount)
        invest.quantity = invest.amount
        invest.gatheredAmount += amount
        invest.balance += amount
        invest.save()
        #
        InvestmentValue = investor.invested_value
        investor.invested_amount += amount
        investor.invested_value += amount
        investor.reinvested = datetime.now()
        investor.save()
        # ** INVESTED_AMOUNT is Negative
        if investor.invested_amount < 0:
            reInvestLowerThanInvestedAmount(investor.id)
        # **
        UpdateAllInvestorPercentage()
        # investor.invested_percentage = float(
        #     investor.invested_amount) / float(invest.amount) * 100
        percentage_after = float(investor.invested_percentage)
        # recording the investment
        recordInvestment(iClubTotalValue, InvestmentAmount, InvestmentValue, investor_id,
                         investor_Name, percentage_before, percentage_after)
        print('\n\n DONE REINVESTING \n')
        # return redirect('invest:records')
        return
    except:
        print('\n CAnt find the user')
        # return redirect('invest:records')
        return


def RecordTheDividend(request):
    TotalInvestmentObject = Total_Investment.objects.get(stock='php')
    investorRatioList = Investor.objects.filter(interestType='ratio')
    for InvestorObject in investorRatioList:
        # ---------
        ProfitAmount = (int(InvestorObject.invested_value) -
                        int(InvestorObject.invested_amount))

        DividendAmount = 0
        print('\n Calculating DIvidend \n')
        DividendAmount += (int(ProfitAmount) *
                           float(InvestorObject.interest/100))

        DividendObject = DividendRecord.objects.create(investorID=InvestorObject.id,
                                                       investedAmount=InvestorObject.invested_amount, investedValue=InvestorObject.invested_value, investedProfit=ProfitAmount, contractRatio=InvestorObject.interest, investedDividend=DividendAmount)
        InvestorObject.invested_value = InvestorObject.invested_amount

        InvestorObject.dividendsReceived.add(DividendObject)
        InvestorObject.save()
        print('\n DON ALL DIVIDENDs \n')
    # TODO CALCULAATE .balance from amount - handinStock
    TotalInvestmentObject.amount = TotalInvestmentObject.gatheredAmount
    TotalInvestmentObject.balance = TotalInvestmentObject.gatheredAmount
    TotalInvestmentObject.save()
    UpdateAllInvestorPercentage()

    return redirect('invest:records')


def reports(request):
    if request.user.is_authenticated:
        # ALSO RECORD DIVIDEND *** DONT DO ALREADY on DividendRecord
        # MAKE IT when re_invest lower than invested_amount
        #     if request.method == 'POST':

        #         investorID = request.POST.get('investorID')
        #         investorUser = Investor.objects.get(pk=investorID)
        # #
        #         investedAmount = investorUser.invested_amount
        #         investedValue = investorUser.invested_value
        #         investedProfit = int(investedValue) - int(investedAmount)
        #         # contractRatio = float(investorUser.interestType.percentage) / 100
        #         contractRatio = 10 / 100
        #         investedDividend = int(contractRatio) * int(investedProfit)

        #         dividendItem = DividendRecord()
        #         dividendItem.investedAmount = investedAmount
        #         dividendItem.investedValue = investedValue
        #         dividendItem.investedProfit = investedProfit
        #         dividendItem.contractRatio = contractRatio
        #         dividendItem.investedDividend = investedDividend
        #         dividendItem.save()
        # #
        #         investorUser.dividendsReceived.add(dividendItem)
        #         print('\n\n DONE ADDING DIVIDEND')
        #         return redirect('invest:reports')

        allInvestors = Investor.objects.all().order_by('invested_amount')
        allInterestTypes = InterestTypes.objects.all()
        context = {
            'allInvestors': allInvestors,
            'allInterestTypes': allInterestTypes
        }
        return render(request, 'commerce/invest/reports.html', context)
