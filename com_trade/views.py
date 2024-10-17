# from . import acs
from django.views.decorators.csrf import csrf_exempt
from binance.client import Client
from django.shortcuts import render

# Create your views here.


def index(request):
    import os
    import requests
    # uncomment Below for News
    apis = requests.get(
        'https://newsapi.org/v2/everything?q=dogecoin&apiKey=b3f57b413e2942cc94bd6609ed38a52f').json()

    variables = {
        'files': os.listdir('./csvs/historicalDatas'),
        # uncomment Below for News
        'latest_news': apis['articles']
    }
    if not request.user.is_authenticated:

        return render(request, "user/login.html", variables)
    return render(request, 'commerce/trade/index.html', variables)


def live_chart(request):
    return render(request, 'commerce/trade/live.html')


def primary_chart(request):
    return render(request, 'commerce/trade/primary_chart.html')


def primary_live(request):
    return render(request, 'commerce/trade/primary_live.html')
# ------------------------


# def open_csv(request):
#     BTCUSDT-Jan. 1, 2021


@csrf_exempt
def new_data(request, what_coin, what_interval):

    file_path = 'csvs/historicalDatas'
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        new_data = data.get("new_date")
    # from binance.client import Client
        import os
        import csv
        import time
        client = Client()
        crypto = what_coin
        starting = new_data
        # intervals
        if what_interval == 'KLINE_INTERVAL_3MINUTE':
            theInterval = Client.KLINE_INTERVAL_3MINUTE
        elif what_interval == 'KLINE_INTERVAL_1MINUTE':
            theInterval = Client.KLINE_INTERVAL_1MINUTE
        elif what_interval == 'KLINE_INTERVAL_15MINUTE':
            theInterval = Client.KLINE_INTERVAL_15MINUTE
        elif what_interval == 'KLINE_INTERVAL_1DAY':
            theInterval = Client.KLINE_INTERVAL_1DAY
        elif what_interval == 'KLINE_INTERVAL_1HOUR':
            theInterval = Client.KLINE_INTERVAL_1HOUR
        elif what_interval == 'KLINE_INTERVAL_12HOUR':
            theInterval = Client.KLINE_INTERVAL_12HOUR

        klines = client.get_historical_klines(
            crypto, theInterval, starting)
        # ---------- SAVING -------- save the fetched data t0 csv
        itsInterval = what_interval[15:]
        filed = f"{crypto}-{starting}_{itsInterval}.csv"
        file_name = os.path.join(file_path, filed)

        csvfile = open(file_name, 'w', newline='')
        candlestick_writer = csv.writer(csvfile, delimiter=',')
        ii = 0  # =counting data
        for candle in klines:
            # candle[0] = candle[0] / 1000
            candlestick_writer.writerow(candle)
            ii += 1
        # print(ii)
        # ---------- READING -------
        from django.http import JsonResponse
        # import csv
        # klines = []
        # with open(file_name, newline='') as csvfile:
        #     kline = csv.reader(csvfile, delimiter=',')
        #     for k in kline:
        #         klines.append(k)
        # fetch_old_data(request, filed)
        return JsonResponse(filed, safe=False)

    # return filed  # = return to filename

    # x, y = acs.key('john')
    # client = Client(x, y)
    # ---------------------------
    # ----- FETCHING ---------
    # ---------------------------
    # from internet

    # importing data from csv


def fetch_old_data(request, old_file):
    import os
    file_path = 'csvs/historicalDatas'

    filename = os.path.join(file_path, old_file)

    # filename = old_file
    from django.http import JsonResponse
    import csv
    klines = []
    with open(filename, newline='') as csvfile:
        kline = csv.reader(csvfile, delimiter=',')
        for k in kline:
            klines.append(k)
    return JsonResponse(klines, safe=False)


# def fetch_data(request):
#     from django.http import JsonResponse
#     start_date = "14 Nov, 2021"
#     klines = client.get_historical_klines("BTCUSDT",
#                                           Client.KLINE_INTERVAL_15MINUTE,
#                                           start_date)
#     # processed_klines = []
#     # for data in klines:
#     #     kline = {
#     #         "time": data[0],
#     #         "open": data[1],
#     #         "high": data[2],
#     #         "low": data[3],
#     #         "close": data[4]
#     #     }
#     #     processed_klines.append(kline)
#     return JsonResponse(klines, safe=False)


# historical trade


def fetch_data(request):
    from django.http import JsonResponse
    history = client.get_historical_trades(symbol='BTCUSDT', limit=50)
    return JsonResponse(history, safe=False)


def fetch_csv():
    from flask import jsonify
    file_date = 'BNBUSDT-15m-Nov 8, 2021.csv'

    def get_file(filename):
        klines = []
        with open(filename, newline='') as csvfile:
            kline = csv.reader(csvfile, delimiter=',')
            for row in kline:
                kline = {
                    "time": int(float(row[0])),
                    "open": row[1],
                    "high": row[2],
                    "low": row[3],
                    "close": row[4],
                }
                klines.append(kline)
        print(klines)
        return klines

    return jsonify(get_file(file_date))

# ******************************
# *********  END FETCH **********
# ******************************
