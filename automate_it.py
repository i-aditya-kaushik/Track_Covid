try:
	from selenium import webdriver
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
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from PIL import Image,ImageDraw,ImageFont
import numpy as np
from tesserocr import PyTessBaseAPI, RIL


import time
import datetime
import csv
import autoit


StateList= [['AN',0],['AP',1], ['AR',0], ['AS',1], ['BR',1], ['CH',0],['CT',1],['DA',0],['DL',1], ['GA',0], ['GJ',1], ['HR',1], ['HP',1], ['JK',1] , ['JH',1], ['KA',1], ['KL',1], ['LA',1], ['MP',1], ['MH',1], ['MN',0],['ML',0] ,['MZ',0], ['NL',0],['OD',1], ['PY',0],['PB',1], ['RJ',1],['SK',1],['TN',1], ['TS',1], ['TR',0], ['UT',1], ['UP',1], ['WB',1]]
c= len(StateList)

def getData():
	driver=webdriver.Chrome('E:/Summer Proj/Covid_Tracker/Code/chromedriver')
	driver.get('https://www.mohfw.gov.in/')
	state_button = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[1]/a[2]/img[1]')
	state_button.click()
	with open('Cases.csv', 'w+', newline='') as file:
		for x in range(c):
			sn = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr['+ str(x+1) +']/td[3]')				  
			writer = csv.writer(file)
			writer.writerow([x+1, StateList[x][0] , sn.text])
		sn = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[36]/td[2]')
		tot = 0
		writer.writerow([x+1, 'ACTIVE CASES:' , sn.text])
		tot+= int(sn.text)
		x+=1
		sn = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[36]/td[4]')
		writer.writerow([x+1, 'CURED CASES:' , sn.text])
		tot+= int(sn.text)
		x+=1
		sn = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[36]/td[6]')
		writer.writerow([x+1, 'DEATHS:' , sn.text])
		tot+= int(sn.text)
		x+=1
		writer.writerow([x+1, 'TOTAL CASES:' , tot])
	driver.quit()


def drawdata():
	s=[[1265, 1927, 'LITERALLY.’'], [1070, 1927, 'HANDS.'], [858, 1927, 'IN YOUR'], [800, 1927, ''], [436, 1927, '‘YOUR SAFETY'], [1408, 1653, 'AN'], [719, 1633, 'KL'], [818, 1618, 'TN'], [308, 1588, 'LK'], [962, 1573, 'PY'], [1462, 1447, 'DEATHS:'], [810, 1402, 'AP'], [1491, 1377, 'XX'], [1322, 1377, 'CURED CASES:'], [646, 1367, 'KA'], [468, 1345, 'GA'], [1319, 1305, 'ACTIVE CASES:'], [1346, 1224, 'TOTAL CASES:'], [863, 1183, 'TS'], [595, 1084, 'MH'], [1166, 1030, 'OD'], [1049, 982, 'CT'], [1555, 893, 'TR'], [1720, 884, 'MZ'], [1333, 866, 'WB'], [787, 859, 'MP'], [1180, 833, 'JH'], [457, 824, 'GJ'], [1444, 764, 'ML'], [1801, 743, 'MN'], [1240, 710, 'BR'], [1792, 668, 'NL'], [1513, 668, 'AS'], [1021, 651, 'UP'], [534, 637, 'RJ'], [823, 529, 'DL'], [666, 529, 'HR'], [1382, 461, 'SK'], [190, 434, 'CH'], [282, 425, 'XX'], [863, 417, 'UT'], [1762, 369, 'AR'], [676, 353, 'PB'], [1269, 318, 'STATEWISE'], [777, 266, 'HP'], [1425, 232, ''], [1338, 232, ''], [1112, 232, ''], [651, 167, 'JK'], [800, 143, 'LA'], [63, 65, ''], [1765, 41, 'updates'], [1620, 41, 'latest'], [936, 41, 'follow @covid_ai_tracker for']]
	image = Image.open('E:/Summer Proj/Covid_Tracker/Code/My_Map.png')
	font_type = ImageFont.truetype('E:/Summer Proj/Covid_Tracker/Code/Helvetica.ttf', 48)
	draw = ImageDraw.Draw(image)

	with open("Cases.csv", "r") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for lines in csv_reader:
			if(lines[1]=='CURED CASES:'):
				cc = int(lines[2])
			if(lines[1]== "TOTAL CASES:"):
				tc = int(lines[2])
			if(lines[1]=="DEATHS:"):
				d = int(lines[2])
			if(lines[1]=='ACTIVE CASES:'):
				ac = int(lines[2])
	for x in range(len(s)):
		with open("Cases.csv", "r") as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for lines in csv_reader:
				if(s[x][2]=='TOTAL CASES:'):
					draw.text(xy = (s[x][0]+350,s[x][1]+5), text= str(tc) , fill =(255,0,0), font = font_type )
					break
				if(s[x][2]=='CURED CASES:'):
					draw.text(xy = (s[x][0]+375,s[x][1]+5), text= str(cc) , fill =(255,0,0), font = font_type )
					break
				if(s[x][2]=='DEATHS:'):
					draw.text(xy = (s[x][0]+235,s[x][1]+5), text= str(d) , fill =(255,0,0), font = font_type )
					break
				if(s[x][2]=='ACTIVE CASES:'):
					draw.text(xy = (s[x][0]+375,s[x][1]+5), text= str(ac) , fill =(255,0,0), font = font_type )
					break
		for y in range(len(StateList)):
			if(s[x][2] == StateList[y][0]):
				with open("Cases.csv", "r") as csv_file:
					csv_reader = csv.reader(csv_file, delimiter=',')
					for lines in csv_reader:
						if(lines[1]== s[x][2]):
							if(StateList[y][1]==1):
								draw.text(xy = (s[x][0]+10,s[x][1]+50), text= lines[2] , fill =(255,255,255), font = font_type )
							if(StateList[y][1]==0):
								draw.text(xy = (s[x][0]+10,s[x][1]+50), text= lines[2] , fill =(0,0,0), font = font_type )
				break
	image.save('My_Map_I.png')

def post_ig():
	mobile_emulation = { "deviceName": "Nexus 5" }
	options = webdriver.ChromeOptions()
	options.add_experimental_option("mobileEmulation", mobile_emulation)
	driver = webdriver.Chrome(chrome_options=options)
	driver.get('https://www.instagram.com/')
	time.sleep(3)
	driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/article[1]/div[1]/div[1]/div[1]/div[2]/button[1]').click()
	time.sleep(4)
	pass_field = driver.find_element_by_xpath("//input[@name='password']")
	pass_field.click()
	pass_field.send_keys('helloitsme123')
	time.sleep(2)
	user_field = driver.find_element_by_xpath("//input[@name='username']")
	user_field.send_keys('track_covid')
	time.sleep(2)
	driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/main[1]/article[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[6]/button[1]").click()
	time.sleep(5)
	driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
	time.sleep(3)
	driver.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
	time.sleep(2)
	driver.find_element_by_xpath("//div[@class='q02Nz _0TPg']//*[local-name()='svg']").click()
	time.sleep(2)
	autoit.control_focus("Open","Edit1")
	autoit.control_set_text("Open","Edit1",'E:\Summer Proj\Covid_Tracker\Code\My_Map_I.png' )
	autoit.control_click("Open","Button1")
	time.sleep(2)
	driver.find_element_by_xpath("//button[@class='UP43G']").click()
	time.sleep(2)
	Caption = driver.find_element_by_xpath("//textarea[@placeholder='Write a caption…']")
	Caption.send_keys('Follow @track_covid for latest updates on the Covid 19 Pandemic. This is an automated software which automatically fetches the data from mohfw.gov.in and edits the photo accordingly. Stay Home, Stay Safe! ')
	time.sleep(2)
	driver.find_element_by_xpath("//button[@class='UP43G']").click()
	time.sleep(6)
	driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
	time.sleep(2)
	driver.find_element_by_xpath("//a[contains(@class,'gKAyB')]//img[@class='_6q-tv']").click()
	time.sleep(3)
	driver.find_element_by_xpath("//div[@class='_9AhH0']").click()
	time.sleep(2)
	driver.find_element_by_xpath("//span[@class='_15y0l']//button[contains(@class,'wpO6b')]//*[local-name()='svg']").click()
	time.sleep(3)
	mess = driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']")
	mess.send_keys('#stayhomesavelives #coronavirus #covid19 #covid #love #instagood #photooftheday #fashion #beautiful #happy #cute #like4like #follow #me #art #instadaily #friends #repost #nature #girl #fun #style #food #intensivecare #wearecritical #covidindia #covidinfo #covidart #covidfreestylechallenge #covidphotodiaries')
	driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
	driver.quit()



getData()
drawdata()
post_ig()
