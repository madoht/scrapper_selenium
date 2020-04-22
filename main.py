import time
from selenium import webdriver
from bs4 import BeautifulSoup
from so import get_jobs

driver = webdriver.Chrome('/Users/apple/Desktop/chrome/chromedriver')
driver.implicitly_wait(3)

word = str(input())

get_jobs(word)