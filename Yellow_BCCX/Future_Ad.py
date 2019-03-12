# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:56:06 2018

@author: LYNCSS
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os, sys, pyautogui, time, imaplib, inspect, email, time

# To access Gmail, you have to apply two step. Step 1: Allow imap. Step 2: low secure access

class FutureWorker: #raymond788055 Aa19910917
    
    def __init__(self, account, password):
        self.Future_account = account
        self.Futur_password = password
        self.ChromeDV_route = "C:\\Users\\LYNCSS\\Google_drive\\WORKSTATION\\Crypto_work\\Yellow_BCCX\\configuration\\webdriver\\chromedriver.exe"
        self.driver = webdriver.Chrome(self.ChromeDV_route)
        self.driver.get("https://adpro.futurenet.club/login")
        self._progress_bar = None
        
    def login(self):
        self.driver.find_element_by_name("email").click()
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(self.Future_account)
        self.driver.find_element_by_name("password").click()
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(self.Futur_password)
        self.driver.find_element_by_name("remember").click()
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(0.5)
        while True:
            cont = self.driver.find_element_by_css_selector("button.btn.ng-binding")
            if cont.text == 'X':
                cont.click()
                pass
                break
            
    def Locate_Bar(self):
        self.driver.set_window_position(0,0)
        self._progress_bar = self.driver.find_element_by_css_selector("div.progress-bar.progress-bar-success")
        y_relat_loc = self._progress_bar.location['y']
        browser_navigation_panel_height = self.driver.execute_script('return window.outerHeight - window.innerHeight;')
        y_abs_coord = y_relat_loc + browser_navigation_panel_height
        x_abs_coord = self._progress_bar.location['x']
        return (x_abs_coord, y_abs_coord)
    
    def watchAd_Unit(self):
        self.driver.find_element_by_link_text(u"打开").click()
        WebDriverWait(self.driver, None).until(EC.presence_of_element_located(By.CSS_SELECTOR, "div.progress-bar.progress-bar-success"))
        tmp_coord = self.Locate_Bar()
        pyautogui.moveTo(tmp_coord[0], tmp_coord[1])
        while True:
            try:
                self.driver.find_element_by_link_text(u"下一则广告").click()
                break
            except:
                time.sleep(0.5)
    
    def watchAd(self, random_parm = 1):
        if random_parm == 1:
            time.sleep(5)
            pyautogui.FAILSAFE = False
            self.driver.find_element_by_link_text(u"观看广告").click()
            pyautogui.moveTo(0, 0)
            screen_width_pixel = 1920
            screen_depth_pixel = 1080
            for mouseY_pos in range(0, screen_depth_pixel, 10):
                find = False
                try:
                    time.sleep(0.5)
                    self.watchAd_Unit()
                    break
                except:
                    try:
                        self.driver.find_element_by_css_selector("div.progress-bar.progress-bar-success")
                        break
                    except:
                        pass
                    for mouseX_pos in range(0, screen_width_pixel, 100):
                        pyautogui.moveTo(mouseX_pos, mouseY_pos)
                        try:
                            time.sleep(0.5)
                            self.watchAd_Unit()
                            find = True
                            break
                        except:
                            try:
                                self.driver.find_element_by_css_selector("div.progress-bar.progress-bar-success")
                                find = True
                                break
                            except:
                                pass
                            pass
                if find == True:
                    break
        time.sleep(40)
        self.driver.find_element_by_link_text(u"下一则广告").click()
                
    def Authenticate(self, num_str):
        self.driver.find_element_by_id("code").click()
        self.driver.find_element_by_id("code").clear()
        self.driver.find_element_by_id("code").send_keys(num_str)
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()
            

class Gmail_reader:
    def __init__(self, Gaccount, Gpassword): # raymond788055@gmail.com qweesd541682
        self.account = Gaccount
        self.password = Gpassword
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com')
        self.imap.login(self.account, self.password)
        
    def ReadLastmail(self):
        self.imap.select()
        result, data = self.imap.search(None, "UNSEEN")
        mail_number = data[0].split()[-1]
        typ, mail_content = self.imap.fetch(mail_number, '(RFC822)')
        before_process = str(mail_content[0][1])
        assert len(before_process.split("FutureAdPro")) > 1
        
        first_process_content = before_process.split('color:green')[-1].split('</big>')[0]
        final_content = ''
        for index in first_process_content:
            try:
                final_content = final_content + str(int(index))
            except:
                pass
        return final_content
    
def GetTime():
    time_str = time.strftime("%H:%M:%S", time.gmtime())
    time_list = time_str.split(":")
    return time_list

def tst_main(F_account, F_password, Gaccount, Gpassword):
    worker = FutureWorker(F_account, F_password)
    worker.login()
    Gworker = Gmail_reader(Gaccount, Gpassword)
    try:
        worker.watchAd()
    except:
        auth_code = Gworker.ReadLastmail()
        worker.Authenticate(auth_code)
        worker.watchAd()
                  
def main(F_account, F_password, G_account, G_password, hour):
    worker = FutureWorker(F_account, F_password)
    worker.login()
    Gworker = Gmail_reader(G_account, G_password)
    now = GetTime()
    while True:
        now = GetTime()
        if ((int(now[0]) == (hour-8)) and (int(now[1]) >= 0) and (int(now[2]) >= 0)):
            break
    for index in range(0, 9):
        try:
            worker.watchAd()
        except :
            auth_code = Gworker.ReadLastmail()
            worker.Authenticate(auth_code)
            worker.watchAd()
            pass
    return 1
