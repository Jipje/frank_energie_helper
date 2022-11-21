import requests
import pandas as pd


def load_price_data():
    query = """query MarketPrices {
    marketPricesElectricity(startDate: "2021-11-21", endDate: "2021-11-22") {
        from
        till
        marketPrice    
    }
    marketPricesGas(startDate: "2021-11-21", endDate: "2021-11-22") {
        till
        from
        marketPrice
    }
    }"""
    headers = {'content-type': 'application/json'}
    response = requests.post('https://graphcdn.frankenergie.nl', json={'query': query}, headers=headers)
    data = response.json()
    df = pd.DataFrame(data['data']['marketPricesElectricity'])
    df['from'] = pd.to_datetime(df['from'], utc=True)
    df['till'] = pd.to_datetime(df['till'], utc=True)
    print(df)


if __name__ == '__main__':
    load_price_data()