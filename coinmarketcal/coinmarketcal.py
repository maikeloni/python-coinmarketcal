import configparser
import json
import requests as r


def getToken():
    config = configparser.ConfigParser()
    config.readfp(open('../config.txt'))
    id = config.get('Coinmarketcal', 'id')
    secret = config.get('Coinmarketcal', 'secret')
    payload = {'grant_type': 'client_credentials', 'client_id': id, 'client_secret': secret}
    response = r.post("https://api.coinmarketcal.com/oauth/v2/token", data=payload)
    print(response.url)
    return json.loads(response.text)


def getCoins(token):
    payload = {'access_token': token}
    coins = r.get("https://api.coinmarketcal.com/v1/coins", params=payload)
    return json.loads(coins.text)


def getCategories(token):
    payload = {'access_token': token}
    categories = r.get("https://api.coinmarketcal.com/v1/categories", params=payload)
    return json.loads(categories.text)


def getEvents(token, page=None, max=None, dateRangeStart=None, dateRangeEnd=None,
              coins=None, categories=None, sortBy=None, showOnly=None):
    payload = {
            "page": page,
            "max": max,
            "dateRangeStart": dateRangeStart,
            "dateRangeEnd": dateRangeEnd,
            "coins": coins,
            "categories": categories,
            "sortBy": sortBy,
            "showOnly": showOnly,
            'access_token': token,
             }

    url = "https://api.coinmarketcal.com/v1/events"
    events = r.get(url, params=payload)
    return json.loads(events.text)
