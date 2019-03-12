# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:22:43 2018

@author: LYNCSS
"""

import requests, pymarketcap, pymysql


class HitAPI:
    
    def __init__(self):
        self._public_key = "93214f908a5b0ad233043194ef19e5ce"
        self._secret_key = "022569dfb3bf4396d9604ce3f0e6db1f"
        self._base_URL = "https://api.hitbtc.com/api/2"
        self._session = requests.Session()
        self._session.auth = (self._public_key, self._secret_key)
        self._market_status = None
        
    def GetMarkStatus(self, currency = None):
        if currency == None:
            market_url = self._base_URL + "/public/ticker"
            self._market_status = self._session.get(market_url).json()
            return self._market_status
        else:
            market_url = self._base_URL + "/public/ticker/" + currency
            self._market_status = self._session.get(market_url).json()
            return self._market_status
        
class Price_Parser:
    
    def __init__(self):
        self._All_exchanges = ["Binance","Bitfinex","Hitbtc","Poloniex","Bittrex","Cryptopia"]
        self._Market_system = pymarketcap.Pymarketcap()
        self._exchanges_data = []
        
    def GetExchange_status(self):
        for index in self._All_exchanges:
            self._exchanges_data.append(self._Market_system.exchange(index))
        return self._exchanges_data
        
        