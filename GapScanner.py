import time
import yfinance as yf
import pandas as pd, timeit
import ray
import datetime
import re
from tickers import getTickers

def getGaps():
    tickers = getTickers()
    yesterday = datetime.date.today() - datetime.timedelta(days = 1)
    @ray.remote
    def get_data_ray(symbol):
        time.sleep(0.001)
        try:
            data = yf.download(symbol, start=yesterday, interval="5m", progress=False, prepost=True)["Close"]
            current = data[-1:].tolist()[0]

            output = re.findall(r'15:[0-9][0-9]:[0-9][0-9]-[0-9][0-9]:[0-9][0-9]    [0.9]*.[0-9]*\n[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] 16:[0-9][0-9]:[0-9][0-9]-[0-9][0-9]:[0-9][0-9]    [0.9]*.[0-9]*',  data.to_string())
            previous = float(output.__str__().split("    ")[2].split("'")[0])

            gap = round(((current - previous)/abs(previous)) * 100, 2)
            return (symbol, gap)
        except:
            return (symbol, 0)
    start_time = timeit.default_timer()
    result_ids = [get_data_ray.remote(s) for s in tickers]
    columns=['Ticker','Gap']
    csv = pd.DataFrame(ray.get(result_ids), columns=columns);
    csv.sort_values(["Gap"],axis=0,ascending=[False],inplace=True)
    csv.reset_index(inplace=True)
    print(f'Completed in: {timeit.default_timer() - start_time} seconds.')
    csv.to_csv("gap.csv")
    csv = csv[:50]
    return csv
