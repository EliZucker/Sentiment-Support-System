# import requests
# from lxml import html
# import re
from robobrowser import RoboBrowser
import pandas as pd
# import sys  
# from lxml import html 
from selenium import webdriver
from selenium.webdriver.common.by import By
import signal
import sys

def login():
	browser.open('https://flightaware.com/account/login')
	forms = browser.get_forms()
	form = forms[8]
	form['flightaware_username'] = "andysknoblock@yahoo.com"
	form['flightaware_password'] = "123456A"
	browser.submit_form(form)


def get_delay_for_flight(link):
	url = link
	driver.get(url)
	delay_descrip = driver.find_element_by_class_name("flightPageArrivalDelayStatus").text.replace("(", "").replace(")", "")
	if(delay_descrip.find("late") is -1):
		return 0
	else:
		return 1
	# print(driver.find_element_by_class_name("flightPageArrivalDelayStatus").text.replace("(", "").replace(")", ""))

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


# def get_flight_delay_data(flight):
# 	links = get_flight_links("JBU101")
# 	# print(links)
# 	delays = 0
# 	tot = 0
# 	for link in links:
# 		delays = delays + get_delay_for_flight(link)
# 		tot = tot + 1

# 	print(delays)
# 	print(tot)
# 	return ***REMOVED***"delayed": delays, "tot": tot***REMOVED***


def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        driver.quit()
        sys.exit(0)

	
signal.signal(signal.SIGINT, signal_handler)
browser = RoboBrowser(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36')
login()
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
links = get_flight_links("JBU101")
# print(links)
delays = 0
tot = 0
for link in links:
	print(link)
	delays = delays + get_delay_for_flight(link)
	tot = tot + 1
	print("Delay: " + str(delays) + " Tot: " + str(tot))


# link = "https://flightaware.com/live/flight/JBU1056/history/20191026/1926Z/MBPV/KJFK"
# get_delay_for_flight(link)
driver.quit()


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