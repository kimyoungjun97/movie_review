from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver',
                          options=options)

url = 'https://klyrics.net/category/korean/'
driver.get(url)
driver.find_element_by_xpath('//*[@id="tdi_63"]/div/div/div/div[1]/div/p[1]')
title1 = driver.find_element_by_xpath('')

