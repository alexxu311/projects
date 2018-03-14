import urllib3
import re
import time
import requests
from bs4 import BeautifulSoup
import html5lib
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#incognito mode
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

#open the browser
browser = webdriver.Chrome(chrome_options=option)  # 用chrome浏览器打开

#webpage link
url = "http://data.eastmoney.com/notices/"
browser.get(url)

#waiting time
time.sleep(5)
#timeout = 20
#try:
#    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='content']")))
#except TimeoutException:
#    print("Timed out waiting for page to load")
#    browser.quit()

p = browser.page_source
soup = BeautifulSoup(p, "lxml")
announcement = soup.find('tbody')


code = announcement.find('td')

