# from . import acs
from binance.client import Client
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'trade/index.html')


# ------------------------

# x, y = acs.key('john')
# client = Client(x, y)
# ---------------------------
# ----- FETCHING ---------
# ---------------------------
# from internet

# importing data from csv


def fetch_datas(request):
    filename = 'BNBUSDT-15m-Nov 1, 2021.csv'
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
