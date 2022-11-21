import requests


def load_price_data():
    query = """query MarketPrices {
    marketPricesElectricity(startDate: "2021-11-21", endDate: "2021-11-22") {
        till
        from
        marketPrice    
    }
    marketPricesGas(startDate: "2021-11-21", endDate: "2021-11-22") {
        from
        till
        marketPrice
    }
    }"""
    headers = {'content-type': 'application/json'}
    response = requests.post('https://graphcdn.frankenergie.nl', json={'query': query}, headers=headers)
    data = response.json()
    print(data)


if __name__ == '__main__':
    load_price_data()