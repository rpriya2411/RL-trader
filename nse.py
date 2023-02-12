# NSEINDIA

import requests
import pandas as pd

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 5000)

class NSE:
    pre_market_categories = ['NIFTY 50', 'Nifty Bank', 'Emerge', 'Securities in F&O', 'Other', 'All']
    # equity_market_categories = [...]
    holidays_categories = ['Clearing', 'Trading']

    def __init__(self):
        self.header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.header)

    def pre_market_data(self, category):
        pre_market_category = {"NIFTY 50":"NIFTY", "Nifty Bank": "BANKNIFTY", "Emerge":"SME",
                                "Securities in F&O":"FO", 
                                "Others": "OTHERS", "All":"ALL"
                                }
        data = self.session.get(f"https://www.nseindia.com/api/market-data-pre-open?key={pre_market_category[category]}", 
                                headers=self.header).json()['data']
        
        new_data = []
        for i in data:
            new_data.append(i['metadata'])
        df = pd.DataFrame(new_data)
        df = df.set_index("symbol", drop=True)
        return df

    def equity_market_data(self, category, symbol_list=False):
        category = category.upper().replace(' ', '%20').replace('&', '%26')
        # print(category)
        # print(self.header)
        # print(self.session)
        data = self.session.get(f"https://www.nseindia.com/api/equity-stockIndices?index={category}",
                                headers=self.header).json()['data']

        df = pd.DataFrame(data)
        print(df.head())
        df.drop(['meta'], axis=1)
        df = df.set_index('symbol', drop=True)
        print(df.columns)
        print(len(df))
        if symbol_list:
            return list(df.index)
        else:
            return df

if __name__ == "__main__":
    nse = NSE()
    df = nse.equity_market_data('NIFTY 50')
    print(df.head())

