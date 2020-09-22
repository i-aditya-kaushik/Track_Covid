try:
	from selenium import webdriver
	from tkinter import *
	from selenium.common.exceptions import NoSuchElementException 
except:
	print('Please wait, we are installing selenium on your machine...')
	from pip._internal import main as pipmain
	from tkinter import *	
	pipmain(['instccall', 'selenium'])
	try:
		from selenium import webdriver
		from selenium.common.exceptions import NoSuchElementException 
	except:
		input("selenium not installed, run 'pip install selenium' command in cmd, press enter to exit and run script again after installation")
		quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from pynput.keyboard import Key, Controller
from shutil import make_archive

import time
import datetime
import csv

driver=webdriver.Chrome('chromedriver')
driver.get('https://en.wikipedia.org/wiki/States_and_union_territories_of_India')
time.sleep(5)
stateList = []

for x in range(28):
	ar= driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[3]/div[4]/div[1]/table[4]/tbody[1]/tr['+str(x+1)+']/td[2]')
	stateList.append(ar.text)

print(stateList)