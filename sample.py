# from niftystocks import ns
from nsepy.symbols import get_symbol_list, get_index_constituents_list
import pandas as pd
import numpy as np
from datetime import date
from nsepy import get_history


df = get_index_constituents_list("NIFTY50")
stock = df['Symbol'].values



def get_data(symbol):
    print('-----------')
    sbin = get_history(symbol=symbol,
                    start=date(2022,12,15),
                    end=date(2023,1,24))
    data = sbin[['Prev Close', 'Open', 'High', 'Low', 'Close']].copy()
    data['Change'] = data.apply(lambda x: 100*(x['High'] - x['Low'])/(0.5*(x['High'] + x['Low'])), axis=1)
    data['Interday_Change'] = data.apply(lambda x: 100*(x['Prev Close'] - x['Close'])/(0.5*(x['High'] + x['Low'])), axis=1) # close to zero
    print(data)
    change = data['Change'].values
    m, s = round(np.mean(change), 3), round(np.std(change), 3)
    print(f"{symbol} : change {m} | {s}")

    change = data['Interday_Change'].values
    m, s = round(np.mean(change), 3), round(np.std(change), 3)
    print(f"{symbol} : change {m} | {s}")

    print('-----------')

for i in stock:
    get_data(i)
# sbin = get_history(symbol='NIFTY 50',
#                    start=date(2023,1,1),
#                    end=date(2023,1,23),
#                    index=True)



