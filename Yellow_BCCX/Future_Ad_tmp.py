# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 23:46:15 2018

@author: LYNCSS
"""
from selenium import webdriver
driver = webdriver.Chrome()

def process():
        driver.get("http://adpro.futurenet.club/confirmlocation")
        driver.find_element_by_id("code").click()
        driver.find_element_by_id("code").clear()
        driver.find_element_by_id("code").send_keys("51423")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.close()
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("raymond788055")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Aa19910917")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        while True:
            cont = driver.find_element_by_css_selector("button.btn.ng-binding")
            if cont.text == 'X':
                cont.click()
                pass
                break
        
        driver.find_element_by_css_selector("button.btn.ng-binding").click()
        driver.find_element_by_link_text(u"观看广告").click()
        driver.find_element_by_css_selector("div.panel-heading").click()
        driver.find_element_by_link_text(u"打开").click()
        progress_bar = driver.find_element_by_css_selector("div.progress-bar.progress-bar-success")
        progress_bar.location
        driver.find_element_by_link_text(u"下一则广告").click()
        times = driver.find_element_by_css_selector("b.ng-binding").text.split('/')
        while not times[0] == times[1]:
        driver.find_element_by_css_selector("b.ng-binding").click()
        driver.find_element_by_css_selector("b.ng-binding").click()
        driver.find_element_by_css_selector("span.ng-binding.ng-scope").click()
        driver.m