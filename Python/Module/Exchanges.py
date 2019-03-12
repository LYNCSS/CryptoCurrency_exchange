# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 23:50:48 2018

@author: LYNCSS
"""

import requests, pymarketcap as Pmarket


class hitbtc:
    
    def __init__(self, api_key = None, api_secret = None):
        self._api_key = api_key
        self._api_secret = api_secret
        self._base_cur = ['USDT']
        self._sec_base_cur = ['USD', 'USDT', 'BTC', 'ETH', 'BNB', 'LTC', 'NEO', 'XMR']
        self._base_url = "https://api.hitbtc.com/api/2"
        self._session = requests.Session()
        self._pymarket = Pmarket.Pymarketcap().exchange('hitbtc')
        self._currencies = self._session.get(self._base_url + "/public/currency").json()
        self._currencies_symbol = []
        self._currencies_markets = []
        self._Error_stat = {}
        for index in self._currencies:
            self._currencies_symbol.append(index['id'])
            
    def GetAvaliable_currencies(self):
        return self._currencies_symbol
    
    def GetMarketStatus(self):
        tmp_error_list = []
        if self._currencies_symbol == []:
            self.GetAvaliable_currencies()
        
        terminal_end_point = "/public/ticker"
        result_json = self._session.get(self._base_url + terminal_end_point).json()
        for index in result_json:
            suc_param = 0
            for inner_index in self._sec_base_cur:
                if index['symbol'].upper().startswith(inner_index):
                    index['symbol'] = inner_index + '-' + index['symbol'].split(inner_index)[-1]
                    suc_param = 1
                elif index['symbol'].upper().endswith(inner_index):
                    index['symbol'] = index['symbol'].split(inner_index)[0] + '-' +inner_index
                    suc_param = 1
                if suc_param == 1:
                    break
                else:
                    pass
            if suc_param == 0:
                tmp_error_list.append(index)
            else:
                pass
        if not tmp_error_list == []:
            self._Error_stat['GetMarket_Error'] = tmp_error_list
            print('Market Error Occur.')
        self._currencies_markets = result_json
        return result_json
        
        
        
    
        
        
class bittrex:
    
    def __init__(self, api_key = None, api_secret = None):
        self._api_key = api_key
        self._api_secret = api_secret
        self._base_cur = ['USDT']
        self._sec_base_cur = ['USD', 'USDT', 'BTC', 'ETH', 'BNB', 'LTC', 'NEO', 'XMR']
        self._base_url = "https://bittrex.com/api/v1.1/"
        self._session = requests.Session()
        self._pymarket = Pmarket.Pymarketcap().exchange('bittrex')
        self._currencies = self._session.get(self._base_url + "public/getcurrencies").json()
        self._currencies_symbol = []
        self._currencies_markets = []
        if self._currencies['success'] == True:
            for index in self._currencies['result']:
                self._currencies_symbol.append(index['Currency'])
        
    def GetAvaliable_currencies(self):
        return self._currencies_symbol
    
    def GetMarketStatus(self):
        if self._currencies_symbol == []:
            self.GetAvaliable_currencies()
        
        terminal_end_point = "/public/getmarketsummaries"
        result_json = self._session.get(self._base_url + terminal_end_point).json()
        if result_json['success'] == True:
            result_json = result_json['result']
        else:
            print('GetmarketError')
            return 0
        
        for index in result_json:
            index['symbol'] = index.pop('MarketName')
            index['symbol'] = index['symbol'].split('-')[1] + '-' + index['symbol'].split('-')[0]
            index['ask'] = index.pop('Ask')
            index['bid'] = index.pop('Bid')
        self._currencies_markets = result_json
        return result_json
        
                
class poloniex:
    
    def __init__(self, api_key = None, api_secret = None):
        self._api_key = api_key
        self._api_secret = api_secret
        self._base_cur = ['USDT']
        self._sec_base_cur = ['USD', 'USDT', 'BTC', 'ETH', 'BNB', 'LTC', 'NEO', 'XMR']
        self._base_url = "https://poloniex.com"
        self._session = requests.Session()
        self._currencies_symbol = []
        self._currencies_markets = []
    
    def GetAvaliable_currencies(self):
        terminal_end_point = "/public?command=returnTicker"
        result = self._session.get(self._base_url + terminal_end_point).json()
        result_keys = list(result.keys())
        for index in result_keys:
            self._currencies_symbol.append(index.split('_')[0])
            self._currencies_symbol.append(index.split('_')[1])
        self._currencies_symbol = list(set(self._currencies_symbol))
        return self._currencies_symbol
    
    def GetMarketStatus(self):
        '''
            Not done with message processing yet
        '''
        tmp_dict = {}
        terminal_end_point = "/public?command=returnTicker"
        result_json = self._session.get(self._base_url + terminal_end_point).json()
        for index in result_json:
            retu_index = index.split('_')[-1] + "-" + index.split('_')[0]
            result_json[index]['ask'] = result_json[index].pop('lowestAsk')
            result_json[index]['bid'] = result_json[index].pop('highestBid')
            tmp_dict = {'symbol' : retu_index}
            tmp_dict = {**tmp_dict, **result_json[index]}
            self._currencies_markets.append(tmp_dict)
        return self._currencies_markets
        
    
    
    
class binance:
    
    def __init__(self):
        self._base_cur = ['USDT']
        self._sec_base_cur = ['USDT','BTC', 'ETH', 'BNB', 'LTC', 'NEO', 'XMR', 'USD']
        self._session = requests.Session()
        self._base_url = "https://api.binance.com"
        self._marketcap = Pmarket.Pymarketcap()
        self._exchange = self._marketcap.exchange('binance')
        self._currencies_symbol = []
        self._Error_stat = {}
    
    def GetAvaliable_currencies(self):
        terminal_point = "/api/v3/ticker/price"
        result = self._session.get(self._base_url + terminal_point).json()
        for index in result:
            suces_param = 0
            for inner_index in self._sec_base_cur:
                if index['symbol'].startswith(inner_index):
                    self._currencies_symbol.append(inner_index)
                    self._currencies_symbol.append(index['symbol'].split(inner_index)[-1])
                    suces_param = 1
                elif index['symbol'].endswith(inner_index):
                    self._currencies_symbol.append(inner_index)
                    self._currencies_symbol.append(index['symbol'].split(inner_index)[0])
                    suces_param = 1
                else:
                    pass
                if suces_param == 1:
                    break
        
        self._currencies_symbol = list(set(self._currencies_symbol))
        return self._currencies_symbol
    
    def GetMarketStatus(self):
        tmp_error_list = []
        if self._currencies_symbol == []:
            self.GetAvaliable_currencies()
            
        terminal_end_point = "/api/v3/ticker/bookTicker"
        result_json = self._session.get(self._base_url + terminal_end_point).json()
        for index in result_json:
            suc_param = 0
            index['ask'] = index.pop('askPrice')
            index['bid'] = index.pop('bidPrice')
            for inner_index in self._sec_base_cur:
                if index['symbol'].upper().startswith(inner_index):
                    index['symbol'] = inner_index + '-' + index['symbol'].split(inner_index)[-1]
                    suc_param = 1
                elif index['symbol'].upper().endswith(inner_index):
                    index['symbol'] = index['symbol'].split(inner_index)[0] + '-' +inner_index
                    suc_param = 1
                if suc_param == 1:
                    break
                else:
                    pass
            if suc_param == 0:
                tmp_error_list.append(index)
            else:
                pass
        if not tmp_error_list == []:
            self._Error_stat['GetMarket_Error'] = tmp_error_list
            print('Market Error Occur.')
        self._currencies_markets = result_json
        return result_json
        
        
    
    
    
class cryptopia:
    
    def __init__(self):
        self._base_cur = ['USDT']
        self._sec_base_cur = ['BTC', 'ETH', 'BNB', 'LTC', 'NEO', 'USDT', 'XMR']
        self._base_url = "https://www.cryptopia.co.nz/api/"
        self._session = requests.Session()
        self._currencies_symbol = []
        self._currencies = self._session.get(self._base_url + "/GetCurrencies").json()
        if self._currencies['Success'] == True:
            for index in self._currencies['Data']:
                self._currencies_symbol.append(index['Symbol'])
    
    def GetAvaliable_currencies(self):
        return self._currencies_symbol
    
    def GetMarketStatus(self):
        terminal_end_point = "GetMarkets"
        result_json = requests.get(self._base_url + terminal_end_point).json()
        
        if result_json['Success'] == True:
            for index in result_json['Data']:
                index['symbol'] = index.pop('Label')
                index['symbol'] = index['symbol'].split('/')[0] + '-' + index['symbol'].split('/')[-1]
                index['bid'] = index.pop('BidPrice')
                index['ask'] = index.pop('AskPrice')
            self._currencies_markets = result_json['Data']
        return result_json['Data']
    
class bitfinex:
    
    def __init__(self):
        self._base_cur = ['USDT']
        self._sec_base_cur = ['BTC', 'ETH', 'BNB', 'LTC', 'NEO', 'USDT', 'XMR']
        self._base_url = "https://api.bitfinex.com/v1"
        self._session = requests.Session()
        self._currencies_symbol = []
                
    def GetAvaliable_currencies(self):
        terminal_end_point = "/symbols_details"
        result = self._session.get(self._base_url + terminal_end_point).json()
        
        for index in result:
            suces_param = 0

            for inner_index in self._sec_base_cur:
                if index['pair'].upper().startswith(inner_index):
                    self._currencies_symbol.append(inner_index)
                    self._currencies_symbol.append(index['pair'].upper().split(inner_index)[-1])
                    suces_param = 1
                elif index['pair'].upper().endswith(inner_index):
                    self._currencies_symbol.append(inner_index)
                    self._currencies_symbol.append(index['pair'].upper().split(inner_index)[0])
                    suces_param = 1
                else:
                    pass
                if suces_param == 1:
                    break
        self._currencies_symbol = list(set(self._currencies_symbol))
        return self._currencies_symbol
    
    def GetMarketStatus(self):
        terminal_end_point = "/book"
        result_json = self._session.get(self._base_url + terminal_end_point).json()
        return result_json