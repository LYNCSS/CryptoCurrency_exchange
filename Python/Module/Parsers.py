# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 09:12:27 2018

@author: LYNCSS
"""

"""
Target exchanges:
    hitbtc, poloniex, bittrex, binance, cryptopia, bitfinex
    最低賣價 : ask
    最高買價 : bid
"""

import os, sys, pymarketcap as Pmarket, requests
import numpy as np, pandas as pd
import time
sys.path.append('C:\\Users\\LYNCSS\\Google_drive\\WORKSTATION\\Crypto_work\\Python\\Module')
import Exchanges


class MarketParser:
    
    def __init__(self):
        
        """
            setup all parameter
        """
        self._target_exchanges = ['hitbtc', 'poloniex', 'bittrex', 'binance', 'cryptopia', 'bitfinex']
        self._Ftarget_exchanges = ['hitbtc', 'poloniex', 'bittrex', 'binance', 'cryptopia', 'bitfinex', 'Huobi']
        self._base_currencies_SB = ['USDT']
        self._currencies_list = []
        self.hitbtcEx = Exchanges.hitbtc()
        self.binanceEx = Exchanges.binance()
        self.bittrexEx = Exchanges.bittrex()
        self.poloniexEx = Exchanges.poloniex()
        self.cryptopiaEx = Exchanges.cryptopia()
        
        self._currencies_list = list(
                set(self.hitbtcEx.GetAvaliable_currencies()) | 
                set(self.poloniexEx.GetAvaliable_currencies()) | 
                set(self.bittrexEx.GetAvaliable_currencies()) | 
                set(self.binanceEx.GetAvaliable_currencies()) | 
                set(self.cryptopiaEx.GetAvaliable_currencies())
                )

        self._base_DataFrame = pd.DataFrame(
                columns = self._currencies_list, 
                index = self._currencies_list
                )
        self._first_base_currencies = ['USDT']
        self._second_base_currencies = ['BTC', 'ETH', 'BNB', 'LTC', 'NEO']
        self._law_currencies = ['USD', 'KRW', 'JPY', 'EUR']
        self._target_currencies = []
        self._law_curr_data = {}
        self._base_curr_data = {}
        self._second_base_curr_data = {}
        self._probable_bridge = {}
        
        self._exchange_datas = {}
        self._price_data = {}
        self._Error_stat = {}
        
        
    def _GetPrices(self):
        self._exchange_datas['cryptopia'] = self.cryptopiaEx.GetMarketStatus()
        self._exchange_datas['hitbtc'] = self.hitbtcEx.GetMarketStatus()
        self._exchange_datas['poloniex'] = self.poloniexEx.GetMarketStatus()
        self._exchange_datas['bittrex'] = self.bittrexEx.GetMarketStatus()
        self._exchange_datas['binance'] = self.binanceEx.GetMarketStatus()
        self._exchange_datas['Grab_time'] = time.ctime()
        
    def _ProcessExchangedata(self):
        tmp_error_stat = {}
        symbol_process_error = []
        index_process_error = []
        index_Type_error = []
        for index in self._exchange_datas:
            print("processing... " + index)
            tmp_null_data_bid = pd.DataFrame(index = self._currencies_list, columns = self._currencies_list)
            tmp_null_data_ask = pd.DataFrame(index = self._currencies_list, columns = self._currencies_list)
            tmp_null_data_vol = pd.DataFrame(index = self._currencies_list, columns = self._currencies_list)
            
            try:
                for sec_index in self._exchange_datas[index]:
                    try:
                        colum_ind = sec_index['symbol'].split('-')[0]
                        index_ind = sec_index['symbol'].split('-')[1]
                    except IndexError:
                        symbol_process_error.append(sec_index)
                    try:
                        tmp_null_data_bid[colum_ind][index_ind] = float(sec_index['bid'])
                        tmp_null_data_ask[colum_ind][index_ind] = float(sec_index['ask'])
                    except KeyError:
                        index_process_error.append(sec_index)
                        pass
                    except TypeError:
                        index_Type_error.append(sec_index)
                        pass
                
                self._price_data[index] = {'bid':tmp_null_data_bid, 'ask': tmp_null_data_ask}
                
            except TypeError:
                self._price_data[index] = self._exchange_datas['Grab_time']
        if not symbol_process_error == []:    
            tmp_error_stat['SymbolProcessError'] = symbol_process_error
        else:
            pass
        if not index_process_error == []:
            tmp_error_stat['IndexProcessError'] = index_process_error
        else:
            pass
        if not tmp_error_stat == {}:
            self._Error_stat['ProcessExchangeDataError'] = tmp_error_stat
        
            
    def _FindOutPair(self, PairSymbol):
        ans = {}
        for index in self._exchange_datas:
            try:
                for inner_index in self._exchange_datas[index]:
                    if inner_index['symbol'] == PairSymbol:
                        ans[index] = inner_index
            except:
                pass
        return ans
            
    def SelectTarget(self, default = 1):
        if default == 1:
            potential_nominee = {'MaxValue' : 0}
            for bid_index in self._price_data:
                for ask_index in self._price_data:
                    print(bid_index)
                    print(ask_index)
                    tmp_result = Compare_frames(self._price_data[bid_index]['bid'], self._price_data[ask_index]['ask'])
                    if tmp_result['MaxValue'] > potential_nominee['MaxValue']:
                        tmp_result['BaseExchange'] = bid_index
                        tmp_result['DestiExchange'] = ask_index
                        potential_nominee = tmp_result
                    else:
                        pass
            return potential_nominee
    
    def Get_market(self):
        self._GetPrices()
        self._ProcessExchangedata()
        return self._price_data


class MarketParserLite:

    def __init__(self):
        self.Law_currencies = ["USD", "KRW", "JPY", "TWD"]
        self.Base_currencies = ["USDT"]
        self.Base_crypto = ["BTC", "ETH", "LTC"]
        self.Target
            





def Compare_frames(frame1, frame2):
    frame1[frame1 == 0] = 1e-9
    delta = abs(frame1 - frame2) / frame1
    delta = delta.fillna(value = -1)
    delta_val = delta.values
    i,j = np.unravel_index(delta_val.argmax(), delta_val.shape)
    
    ind = delta.index
    max_val = delta.iloc[i, j]
    return {'MaxValue':max_val, 'SymbolPair':(ind[j] + "-" + ind[i])}


    
    
    