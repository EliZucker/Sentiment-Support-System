# import requests
# from lxml import html
# import re
from robobrowser import RoboBrowser
import pandas as pd
# import sys  
# from lxml import html 
from selenium import webdriver
from selenium.webdriver.common.by import By

def login():
	browser.open('https://flightaware.com/account/login')
	forms = browser.get_forms()
	form = forms[8]
	form['flightaware_username'] = "areuter12003310@gmail.com"
	form['flightaware_password'] = "123456A"
	browser.submit_form(form)


def get_delay_for_flight(link):
	url = link
	driver.get(url)
	print(driver.find_element_by_class_name("flightPageArrivalDelayStatus").text.replace("(", "").replace(")", ""))
	driver.quit()

def get_flight_links(flight):
	url = "https://flightaware.com/live/flight/" + str(flight) + "/history/80"
	driver.get(url)
	elmnts = driver.find_elements(By.XPATH, "//span[contains(@class, 'tablesaw-cell-content')]/a")

	links = []
	for x in elmnts:
		# print(x.get_attribute('outerHTML')[9:-17])
		links.append("https://flightaware.com" + x.get_attribute('outerHTML')[9:-17])

	return links
	# print(driver.find_elements(By.XPATH, "//span[contains(@class, 'tablesaw-cell-content')]/a"))
	# print(find_elements_by_xpath("//span[contains(@class, 'tablesaw-cell-content')]"))
	# print(driver.find_elements_by_class_name("tablesaw-cell-content"))


browser = RoboBrowser(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36')
login()
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
print(get_delay_for_flight("https://flightaware.com/live/flight/JBU101/history/20191027/2321Z/KFLL/KLAX"))
print(get_flight_links("JBU101"))

# driver = webdriver.PhantomJS()
# driver.set_window_size(1120, 550)
# get_delay_for_flight("JBU101","KFLL","KLAX", "20191024", "2334Z")

'''
<div class="flightPageDestinationDelayStatus">
									<span class="flightPageArrivalDelayStatus delayed">(34 minutes late)</span>
								</div>


								<span class="flightPageSummaryArrival flightTime" data-flightid="afea6e6f2d1932cbb863a73c1695024aa4ef09536d7c7472f583811cec3226a2" data-type="arrival">
					
					10:29PM PDT
					
								<div class="flightPageDestinationDelayStatus">
									<span class="flightPageArrivalDelayStatus delayed">(34 minutes late)</span>
								</div>
				</span>
'''
# //*[@id="flightPageTourStep1"]/div[3]/div[2]/span[3]/div/span
# /div/div[3]/div[2]/span[3]/div/span
# /html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/span[3]/div/span