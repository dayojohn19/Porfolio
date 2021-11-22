from datetime import datetime
import pandas as pd

last_day_of_current_year = datetime.now().date().replace(month=12, day=31)


with open(("mtn_mtx.txt").lower(), "r") as rfile:
    next(rfile)

    for line in rfile:
        line = line.rstrip('\n')
        line = line.upper()
        line = line.split('\t')

        firstcoupondate = (line[5])

        month_list = [i.strftime("%Y-%m-%d") for i in pd.date_range(
            start=firstcoupondate, end=last_day_of_current_year, freq='MS')]

        print(month_list)
