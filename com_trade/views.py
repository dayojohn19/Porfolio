# from . import acs
from django.views.decorators.csrf import csrf_exempt
from binance.client import Client
from django.shortcuts import render

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "user/login.html")
    return render(request, 'commerce/trade/index.html')


def live_chart(request):
    return render(request, 'commerce/trade/live.html')


def primary_chart(request):
    return render(request, 'commerce/trade/primary_chart.html')
# ------------------------

# def open_csv(request):
#     BTCUSDT-Jan. 1, 2021


@csrf_exempt
def new_data(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        new_data = data.get("new_date")
    # from binance.client import Client

        import csv
        import time
        client = Client()
        crypto = 'BTCUSDT'
        # starting = 'Nov 18, 2021'
        starting = new_data
        # intervals
        # KLINE_INTERVAL_12HOUR
        # KLINE_INTERVAL_15MINUTE
        # KLINE_INTERVAL_3DAY
        # KLINE_INTERVAL_1DAY
        klines = client.get_historical_klines(
            crypto, Client.KLINE_INTERVAL_1DAY, starting)
        # ---------- SAVING -------- save the fetched data t0 csv
        filed = f"{crypto}-{starting}"

        csvfile = open(f"{filed}.csv", 'w', newline='')
        candlestick_writer = csv.writer(csvfile, delimiter=',')
        ii = 0  # =counting data
        for candle in klines:
            # candle[0] = candle[0] / 1000
            candlestick_writer.writerow(candle)
            ii += 1
        # print(ii)
        # ---------- READING -------
        filename = f'{filed}.csv'
        from django.http import JsonResponse
        import csv
        klines = []
        with open(filename, newline='') as csvfile:
            kline = csv.reader(csvfile, delimiter=',')
            for k in kline:
                klines.append(k)
        return JsonResponse(klines, safe=False)

    # return filed  # = return to filename

    # x, y = acs.key('john')
    # client = Client(x, y)
    # ---------------------------
    # ----- FETCHING ---------
    # ---------------------------
    # from internet

    # importing data from csv


def fetch_datas(request):
    filename = 'BTCUSDT-Jan. 1, 2021.csv'
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
