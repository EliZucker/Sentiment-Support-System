import requests
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import signal
import sys
import json
import time

def login():
	driver.get('https://flightaware.com/account/login')
	driver.find_element_by_name("flightaware_username").send_keys("andysknoblock@yahoo.com")
	driver.find_element_by_name("flightaware_password").send_keys("123456A")
	driver.find_element_by_class_name("actionButton").click()

def get_flights_per_carrier(carrier):
	allflights = []
	base = "https://flightaware.com/live/fleet/" + carrier

	for x in range(20, 120, 20):
		end = "?;offset=" + str(x) + ";order=ident;sort=ASC"
		page = requests.get(base + end)
		flights = re.findall(carrier + "[0-9]+", page.text)
		skip = False
		for f in flights:
			if(skip):
				skip = False
				continue
			else:
				skip = True
				allflights.append(f)

	return allflights

def get_delay_for_flight(link):
	url = link
	driver.get(url)
	try:
		delay_descrip = driver.find_element_by_class_name("flightPageArrivalDelayStatus").text.replace("(", "").replace(")", "")
		if(delay_descrip.find("late") is -1):
			return 0
		else:
			return 1
	except Exception as e:
		print(e)
		print(driver.page_source)
		with open('response.html', 'w') as file:
			file.write(json.dumps(driver.page_source))
		print("Waiting 5 seconds")
		time.sleep(5)
		return get_delay_for_flight(link)
	# print(driver.find_element_by_class_name("flightPageArrivalDelayStatus").text.replace("(", "").replace(")", ""))

def get_flight_links(flight):
	url = "https://flightaware.com/live/flight/" + str(flight) + "/history/80"
	driver.get(url)
	print("url loaded")
	elmnts = driver.find_elements(By.XPATH, "//span[contains(@class, 'tablesaw-cell-content')]/a")
	#Now I also need the date with each link

	links = []
	for x in elmnts:
		# print(x.get_attribute('innerHTML'))
		# print(x.get_attribute('outerHTML')[9:-17])
		links.append(***REMOVED***"date": x.get_attribute('innerHTML'), "link": "https://flightaware.com" + x.get_attribute('outerHTML')[9:-17]***REMOVED***)
	# print("processing done")
	return links
	# print(driver.find_elements(By.XPATH, "//span[contains(@class, 'tablesaw-cell-content')]/a"))
	# print(find_elements_by_xpath("//span[contains(@class, 'tablesaw-cell-content')]"))
	# print(driver.find_elements_by_class_name("tablesaw-cell-content"))


#return ***REMOVED***"25-oct-2019": ***REMOVED***"delays": 0, "tot": 0***REMOVED******REMOVED***
def get_flight_delay_data(flight, storage):
	# data = ***REMOVED******REMOVED***
	links = get_flight_links(flight)
	# print(links)
	delays = 0
	tot = 0
	for link in links:
		print(link)
		datum = storage.get(link["date"], ***REMOVED***"delays": 0, "tot": 0***REMOVED***)
		datum["delays"] = datum["delays"] + get_delay_for_flight(link["link"])
		datum["tot"] = datum["tot"] + 1
		storage[link["date"]] = datum

def get_carrier_data(carrier):
	overall = ***REMOVED******REMOVED***
	flights = get_flights_per_carrier(carrier)
	print(flights)
	for flight in flights:
		print(flight)
		get_flight_delay_data(flight, overall)
		print(overall)
		write_to_file(overall)

def write_to_file(dictionary):
	with open('data.txt', 'w') as file:
	     file.write(json.dumps(dictionary))


def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        driver.quit()
        sys.exit(0)

	
signal.signal(signal.SIGINT, signal_handler)
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
login()
print(get_carrier_data("JBU"))
# links = get_flight_links("JBU101")
# print(links)
# delays = 0
# tot = 0
# for link in links:
# 	print(link)
# 	delays = delays + get_delay_for_flight(link)
# 	tot = tot + 1
# 	print("Delay: " + str(delays) + " Tot: " + str(tot))


# print(get_flight_delay_data("JBU101"))
# get_flight_links("JBU101")
# get_carrier_data("JBU")



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