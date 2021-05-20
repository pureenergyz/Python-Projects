import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from mailer import Mailer

def product():
	driver = webdriver.Chrome('C:/Users/Me/Documents/PY/chromedriver.exe')
	driver.get("https://the website you want to monitor pricing")
	driver.save_screenshot("pic.png")
	time.sleep(2)
	bv = driver.find_element_by_xpath('Xpath found at website').text
	bv = float(bv.replace("$", ""))
	bv = int(bv)
	v = 2499 # The price you want above or below to be alerted at.
	if bv < v:	
		mail = Mailer(email='youremail@gmail.com', password='password')
		mail.send(receiver='youremail@yahoo.com', subject='ALERT', message='Time to Buy!!!!', image='C:/Users/Me/Documents/PY/pic.png')

	else:
		print(False)
	driver.close()





product()

while True:
	product()
	time.sleep(5000)