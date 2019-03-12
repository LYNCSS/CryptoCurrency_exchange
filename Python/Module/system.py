# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 12:56:01 2018

@author: LYNCSS
"""

import os, sys, pymarketcap as Pmarket
import time
import ccxt

class Parser:
    
    def __init__(self):
        self.system = Pmarket.Pymarketcap()
        self.object_currency = None
        self.records = []
        self.excnahges = None
        self.prices = None
        self._processed_data = []
        self._AllCurrency = []
        tmp = self.system.ticker()
        for index in tmp:
            self._AllCurrency.append(index['symbol'])
        
    
    def GetInfo(self, currency = None):
        if currency == None:
            self.object_currency = 1
            for index in self._AllCurrency:
                self.records.append(self.system.markets(index))
        elif type(currency) == str:
            tmp = self.system.ticker(currency)
            self.object_currency = tmp['symbol']
            self.records = self.system.markets(self.object_currency)
        return self.records

    def FindProperExchanges(self):
        try:
            Avaliable_price = []
            for index in self.records:
                if (index['24h_volume_usd'] >= 100000) and ((index['pair'].endswith('BTC')) or (index['pair'].endswith('ETH')) or (index['pair'].endswith('LTC'))) and (index['updated'] == True):
                    self._processed_data.append(index)
                    Avaliable_price.append(index['price_usd'])
            Exchange_BuyFrom = self._processed_data[Avaliable_price.index(min(Avaliable_price))]['exchange']
            Exchange_SellTo = self._processed_data[Avaliable_price.index(max(Avaliable_price))]['exchange']
            return {'BuyFrom' : Exchange_BuyFrom, 'SellTo' : Exchange_SellTo, 'PriceGap': max(Avaliable_price) - min(Avaliable_price)}
        
        except:
            pass
        return 1
        

class Poloniex:
    
    def __init__(self):
        self.apiKey = '5KU93LPQ-2WEZG6OQ-MNEO7YED-NTHVI6HE'
        self.secret = '2774e4eeae78ef53615b8f391cdc3f83539c5c2ab0574d74b43eeae99a919b362729a7ef2619b61dd05bbb3f83f514ac75851f2e306b8a062c8dac0a1b240387'
        self.BTC_wallet_address = ''
        self.system = ccxt.poloniex({'apiKey':self.apiKey, 'secret':self.secret})
        return self.system

class Hitbtc:
    def __init__(self):
        self.apiKey = '93214f908a5b0ad233043194ef19e5ce'
        self.secret = '022569dfb3bf4396d9604ce3f0e6db1f'
        self.BTC_wallet_address = '3Mo9mpx3qPE92V3X3QsovHW1qe2oRc4bKa'
        self.ETH_wallet_address = '0xc24b6dbcd9e466a3670e1d40c2fbdec7b73d0454'
        self.XRP_destination = '880901606'
        self.XRP_wallet_address = 'rhL5Va5tDbUUuozS9isvEuv7Uk1uuJaY1T'
        self.system = ccxt.hitbtc2({'apiKey':self.apiKey, 'secret': self.secret})
        return self.system

class Binance:
    
    def __init__(self):
        self.apiKey = '9ssKoDEB0f3ohk979soe4uplgxHgldeLC6YsoO8w4URyglCFpLB8WPbkTQ2IGuZB'
        self.secret = 'X8ICXkIa5KbZSEyNDaThyQwlxdQffpMgK393FYdUiB4DJ4gNVxITn23SAJMOqfN8'
        self.system = ccxt.binance({'apiKey':self.apiKey, 'secret':self.secret})
        return self.system
    
    

class Bithumb:
    
    def __init__(self):
        self.apiKey = 'c3b5c58d0df366107bba082778187820'
        self.secret = 'bbafea93a44de216f1038bdd09ae31e4'
        self.system = ccxt.bithumb({'apiKey': self.apiKey, 'secret' : self.secret})
        return self.system