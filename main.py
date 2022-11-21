import requests
import pandas as pd
import datetime as dt


def load_price_data(day: dt.datetime | dt.date = None):
    """
    load_price_data will call the Frank Energie API to access market price data.
    :param day: dt.date or datetime object with the day of the energy prices. Default is tomorrow.
    :return: DataFrame with 3 columns, from, till and marketPrice. Specifying prices for time blocks
    """
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
    # TODO handle marketPricesGas
    df = pd.DataFrame(data['data']['marketPricesElectricity'])
    df['from'] = pd.to_datetime(df['from'], utc=True)
    df['till'] = pd.to_datetime(df['till'], utc=True)
    return df


if __name__ == '__main__':
    print(load_price_data(dt.date(2022, 11, 20)))
