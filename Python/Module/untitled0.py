# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:00:13 2018

@author: LYNCSS
"""

import requests

class WebParser:
    
    def __init__(self):
        self._mother_SiteURL = "https://coinmarketcap.com/currencies/"
        self._mother_page = requests.get(self._mother_SiteURL)
        self.Currency_names = 
        return 1
    def getprice(self, currency_name = ""):
        Currency_URL = self.mother_SiteURL + currency_name
        return 1