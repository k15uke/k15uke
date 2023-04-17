print('Twitter Freezer 1.0 by HM3')
print('')
print('必要ライブラリの読み込み中')
import time
print('時間ライブラリをロードしました')
import datetime
print('月日判定ライブラリをロードしました')
import random
print('ランダム変数をロードしました')
import json
print('jsonライブラリをロードしました')
import os
print('osライブラリをロードしました')
import sys
print('システムライブラリをロードしました')
import re
print('整合性ライブラリをロードしました')
import openpyxl
print('Excelライブラリをロードしました')
from lxml import html
print('サイト分析パッケージをロードしました')
from bs4 import BeautifulSoup
print('追加サイト分析ライブラリをロードしました')
from selenium import webdriver
print('Chrome自動操縦ライブラリをロードしました')
import chromedriver_autoinstaller
print('Chrome自動更新ライブラリをロードしました')
from selenium.webdriver.common.by import By
print('時間ライブラリをロードしました')
from webdriver_manager.chrome import ChromeDriverManager
print('Chrome管理ライブラリをロードしました')
from selenium.webdriver.chrome.options import Options
print('Chromeオプションをロードしました')
from selenium.webdriver.support.ui import WebDriverWait
print('読込判定ライブラリをロードしました')
from selenium.webdriver.common.action_chains import ActionChains
print('アクションチェックライブラリをロードしました')
from tkinter import messagebox
print('ポップアップライブラリをロードしました')
from helium import *
print('操縦簡易化モジュールをロードしました')
import shutil
print('ファイル操作ライブラリをロードしました')
from selenium.webdriver.support.ui import Select
print('UI判定ライブラリをロードしました')
print('初期値がセットされました')
print('準備完了')
print('')
os.system('cls')
chrome_noheadless = 1
fail_count = 0
if os.name == 'nt':
    operation ='Windows'
elif os.name == 'posix':
    operation = 'Mac'
    
def chrome_init():
    global driver,select_mode
    try:
        chrome_ver1 = chromedriver_autoinstaller.get_chrome_version().split('.')[0]    
        chrome_ver2 = chromedriver_autoinstaller.get_chrome_version().split('.')[1]
        chrome_ver3 = chromedriver_autoinstaller.get_chrome_version().split('.')[2]
        chrome_ver = chrome_ver1 + '.' + chrome_ver2 + '.' + chrome_ver3
        print('Google Chrome インストール確認完了 Ver'+chrome_ver)
        if operation == 'Mac':
            chrome_exists = os.path.exists('chromedriver')
        else:
            chrome_exists = os.path.exists('chromedriver.exe')
        if chrome_exists == True:
            print('ChromeDriver準備完了(既に存在)')
        else:
            try:
                print('ChromeDriverのダウンロード中')
                chrome_path = './'
                ChromeDriverManager(path=chrome_path).install()
                print('ChromeDriverの準備中')
                if operation == 'Windows':
                    shutil.move('.wdm/drivers/chromedriver/win32/'+chrome_ver+'/chromedriver.exe','./chromedriver.exe')
                else:
                    shutil.move('.wdm/drivers/chromedriver/mac64/'+chrome_ver+'/chromedriver','./chromedriver')
                print('ChromeDriverの準備完了')
            except Exception as E:
                print('申し訳ございません。ChromeDriverの準備中にエラーが発生しました。\n再試行するか、以下を開発者へお送りください')
                print(E)
                i = input('何らかのキーを押して終了')
        options = Options()
        try:
            if operation == 'Windows':
                options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe" 
            #options.binary_location = "./chromedrive.exe"
            options.add_argument('--no-sandbox')
            if chrome_noheadless == 1:
                pass
            else:
                options.add_argument('--headless')
            url = 'https://twitter.com'
            driver = start_chrome(url,options=options)
            driver.set_window_size(1920,1080)
            print('Chrome起動完了')        
        except:
            if operation == 'Windows':
                options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            #options.binary_location = "./chromedriver.exe"
            options.add_argument('--no-sandbox')
            if chrome_noheadless == 1:
                pass
            else:
                options.add_argument('--headless')   
            url = 'https://twitter.com'
            driver = start_chrome(url,options=options)
            driver.set_window_size(1920,1080)
            print('Chrome起動完了(32bit、トラブル防止のため64bit版への移行推奨)')
    except Exception as E:
        print('申し訳ございません。Chromeの調査中にエラーが発生しました。継続できません\n以下を開発者へお送りください。')
        print(E)
        i = input('何かのキーを押して終了')
        #exit()
        
def getTweet():
    URLlist = []
    userid = input('凍結させたいユーザーIDを入力してください：')
    driver.get('https://twitter.com/'+userid)
    driver.implicitly_wait(10)
    time.sleep(3)
    htmls = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(htmls,'lxml')
    pattern = re.compile(r'\d{19}')
    progress_url = '/'+userid+'/status/\d{19}'
    for scroll in range(1000):
        htmls = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(htmls,'lxml')
        for TweetURLs in soup.find_all('a',href=re.compile(progress_url)):
            TweetURL = TweetURLs['href']
            TweetURL = TweetURL.replace('/photo/1','')
            TweetURL = TweetURL.replace('analytics','')
            print(TweetURL)
            TweetURL_progress = 'https://twitter.com' + TweetURL
            URLlist.append(TweetURL_progress)
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    for urls in URLlist:
        driver.get(urls)
        time.sleep(3)
        
if __name__ == '__main__':
    chrome_init()
    getTweet()