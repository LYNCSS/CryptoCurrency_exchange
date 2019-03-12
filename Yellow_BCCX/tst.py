# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:35:04 2018

@author: LYNCSS
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os, sys

class BCCX_Autobuy_system:
    
    def __init__(self):
        self.driver = webdriver.Chrome('C:\\Users\\LYNCSS\\Google_drive\\WORKSTATION\\Crypto_work\\Yellow_BCCX\\configuration\\webdriver\\chromedriver.exe')
        self.driver.get("https://bitconnectx.co/dashboard")
        
    def Buy(self):
        self.driver.get("https://bitconnectx.co/dashboard")
        self.driver.find_element_by_id("payment_quantity").click()
        self.driver.find_element_by_id("payment_quantity").clear()
        self.driver.find_element_by_id("payment_quantity").send_keys("30.87456992")
        self.driver.find_element_by_id("payment_type").click()
        Select(self.driver.find_element_by_id("payment_type")).select_by_visible_text("BCC")
        self.driver.find_element_by_css_selector("option[value=\"bcc\"]").click()
        self.driver.find_element_by_id("verify").click()
        self.driver.find_element_by_id("btn-buy-bccx").click()
        self.driver.find_element_by_id("buy-bccx-confirm").click()