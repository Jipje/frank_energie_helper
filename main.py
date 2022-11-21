import requests
import pandas as pd
import datetime as dt


def load_price_data(day: dt.datetime | dt.date = None):
    if day is None:
        day = dt.date.today() + dt.timedelta(days=1)
    day_str = day.strftime('%Y-%m-%d')

    query = f"""query MarketPrices {{
    marketPricesElectricity(startDate: "{day_str}", endDate: "{day_str}") {{
        from
        till
        marketPrice    
    }}
    marketPricesGas(startDate: "{day_str}", endDate: "{day_str}") {{
        till
        from
        marketPrice
    }}
    }}"""
    headers = {'content-type': 'application/json'}
    response = requests.post('https://graphcdn.frankenergie.nl', json={'query': query}, headers=headers)
    data = response.json()
    df = pd.DataFrame(data['data']['marketPricesElectricity'])
    df['from'] = pd.to_datetime(df['from'], utc=True)
    df['till'] = pd.to_datetime(df['till'], utc=True)
    print(df)


if __name__ == '__main__':
    load_price_data(dt.date(2022, 11, 20))
