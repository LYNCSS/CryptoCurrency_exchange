# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 00:23:11 2018

@author: LYNCSS
"""

import requests, pymysql


class StarMove:
    
    def __init__(self):
        self.hitbtc

class Hitbtc:
    
    def __init__(self):
        self._Exchage_name = 'hitbtc'
        self._initEndpoint = 'https://api.hitbtc.com/api/2'
        self._apiKey = None
        self._secretKey = None
        self._session = requests.Session()
        self._DBconnect = pymysql.Connect(host = '127.0.0.1',
                                          user = 'root', 
                                          password = 's6163693', 
                                          database = 'brickmove',
                                          port = 3305)
        self._DBcursor = self._DBconnect.cursor()
   
    def Auth(self, apiKey, secret):
        
         
    def GetMarket(self, default = True):
        if default:
            