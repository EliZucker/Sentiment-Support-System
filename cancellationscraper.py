import requests
from lxml import html
import re
from robobrowser import RoboBrowser
import pandas as pd

carriers = ["JBU","DAL", "AAL", "UAL", "SWA", "NKS"]

'''
***REMOVED***'25-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 172***REMOVED***, '24-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 166***REMOVED***, '21-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 162***REMOVED***, '20-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 168***REMOVED***, '18-Oct-2019': ***REMOVED***'cancelled': 2, 'tot': 188***REMOVED***, '14-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 174***REMOVED***, '13-Oct-2019': ***REMOVED***'cancelled': 4, 'tot': 162***REMOVED***, '11-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 142***REMOVED***, '10-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 164***REMOVED***, '07-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 156***REMOVED***, '06-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 162***REMOVED***, '04-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 170***REMOVED***, '03-Oct-2019': ***REMOVED***'cancelled': 4, 'tot': 160***REMOVED***, '30-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 166***REMOVED***, '29-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 156***REMOVED***, '27-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 164***REMOVED***, '26-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 156***REMOVED***, '23-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 166***REMOVED***, '22-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 164***REMOVED***, '20-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 166***REMOVED***, '19-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 160***REMOVED***, '16-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 168***REMOVED***, '15-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 162***REMOVED***, '13-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 174***REMOVED***, '12-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 146***REMOVED***, '09-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 162***REMOVED***, '08-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 154***REMOVED***, '06-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 162***REMOVED***, '05-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 162***REMOVED***, '03-Sep-2019': ***REMOVED***'cancelled': 46, 'tot': 158***REMOVED***, '02-Sep-2019': ***REMOVED***'cancelled': 44, 'tot': 130***REMOVED***, '01-Sep-2019': ***REMOVED***'cancelled': 4, 'tot': 146***REMOVED***, '31-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 142***REMOVED***, '30-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 152***REMOVED***, '29-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 150***REMOVED***, '28-Aug-2019': ***REMOVED***'cancelled': 2, 'tot': 140***REMOVED***, '27-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 146***REMOVED***, '26-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 148***REMOVED***, '25-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 152***REMOVED***, '24-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 154***REMOVED***, '23-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 158***REMOVED***, '22-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 162***REMOVED***, '20-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 146***REMOVED***, '19-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 168***REMOVED***, '17-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 144***REMOVED***, '16-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 158***REMOVED***, '15-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 160***REMOVED***, '14-Aug-2019': ***REMOVED***'cancelled': 2, 'tot': 130***REMOVED***, '13-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 138***REMOVED***, '12-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 154***REMOVED***, '11-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 150***REMOVED***, '10-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 152***REMOVED***, '09-Aug-2019': ***REMOVED***'cancelled': 2, 'tot': 164***REMOVED***, '07-Aug-2019': ***REMOVED***'cancelled': 10, 'tot': 84***REMOVED***, '06-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 72***REMOVED***, '04-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 64***REMOVED***, '02-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 54***REMOVED***, '01-Aug-2019': ***REMOVED***'cancelled': 2, 'tot': 64***REMOVED***, '30-Jul-2019': ***REMOVED***'cancelled': 0, 'tot': 46***REMOVED***, '29-Jul-2019': ***REMOVED***'cancelled': 0, 'tot': 44***REMOVED***, '28-Jul-2019': ***REMOVED***'cancelled': 0, 'tot': 46***REMOVED***, '27-Jul-2019': ***REMOVED***'cancelled': 0, 'tot': 44***REMOVED***, '26-Jul-2019': ***REMOVED***'cancelled': 2, 'tot': 40***REMOVED***, '25-Jul-2019': ***REMOVED***'cancelled': 0, 'tot': 16***REMOVED***, '27-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 132***REMOVED***, '23-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 122***REMOVED***, '22-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 118***REMOVED***, '17-Oct-2019': ***REMOVED***'cancelled': 8, 'tot': 146***REMOVED***, '16-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 120***REMOVED***, '15-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 120***REMOVED***, '09-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 122***REMOVED***, '08-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 124***REMOVED***, '02-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 124***REMOVED***, '01-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 114***REMOVED***, '25-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 124***REMOVED***, '24-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 112***REMOVED***, '18-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 122***REMOVED***, '17-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 112***REMOVED***, '11-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 128***REMOVED***, '10-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 114***REMOVED***, '04-Sep-2019': ***REMOVED***'cancelled': 14, 'tot': 114***REMOVED***, '21-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 134***REMOVED***, '18-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 132***REMOVED***, '08-Aug-2019': ***REMOVED***'cancelled': 24, 'tot': 146***REMOVED***, '05-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 54***REMOVED***, '03-Aug-2019': ***REMOVED***'cancelled': 0, 'tot': 56***REMOVED***, '31-Jul-2019': ***REMOVED***'cancelled': 10, 'tot': 42***REMOVED***, 'More Past F': ***REMOVED***'cancelled': 0, 'tot': 120***REMOVED***, '26-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 132***REMOVED***, '19-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 136***REMOVED***, '12-Oct-2019': ***REMOVED***'cancelled': 6, 'tot': 160***REMOVED***, '05-Oct-2019': ***REMOVED***'cancelled': 0, 'tot': 134***REMOVED***, '28-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 128***REMOVED***, '21-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 124***REMOVED***, '14-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 124***REMOVED***, '07-Sep-2019': ***REMOVED***'cancelled': 0, 'tot': 122***REMOVED******REMOVED***
'''

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

def get_all_carriers_flights(carriers):
	flights = []
	for carrier in carriers:
		carr_flights = get_flights_per_carrier(carrier)
		for f in carr_flights:
			flights.append(f)

	return flights

def get_carrier_cancellation_stats(carrier):
	carrier_stats = ***REMOVED******REMOVED***
	flights = get_flights_per_carrier(carrier)
	# print("tot: " + str(len(flights)))
	for f in flights:
		f_stats = get_cancelled(f)
		# print(f_stats)
		for date in f_stats.keys():
			datum = carrier_stats.get(date, ***REMOVED***"cancelled":0, "tot":0***REMOVED***)
			# print("Pre: " + str(date) + " " + str(datum))
			datum["cancelled"] = datum["cancelled"] + f_stats[date]["cancelled"]
			datum["tot"] = datum["tot"] + f_stats[date]["tot"]
			# print("Post: " + str(date) + " " + str(datum))
			carrier_stats[date] = datum
		# print(carrier_stats)

	return carrier_stats


def login():
	browser.open('https://flightaware.com/account/login')
	forms = browser.get_forms()
	form = forms[8]
	form['flightaware_username'] = "areuter12003310@gmail.com"
	form['flightaware_password'] = "123456A"
	browser.submit_form(form)

def get_cancelled(flight):
	url = "https://flightaware.com/live/flight/" + str(flight) + "/history/80"
	print(url)
	browser.open(url)
	html = str(browser.parsed)
	data = pd.read_html(html)[2]
	stored = ***REMOVED******REMOVED***

	for x in range(3, data.shape[0], 1):
		date = str(data.iloc[x,[0]])[8:19]
		duration = str(data.iloc[x,[6]])[12:16]

		datum = stored.get(date, ***REMOVED***"cancelled":0, "tot": 0***REMOVED***)

		if(duration == "Canc"):		
			datum["cancelled"] = datum["cancelled"] + 1
			datum["tot"] = datum["tot"] + 1
			stored[date] = datum
		else:
			datum["tot"] = datum["tot"] + 1
			stored[date] = datum

			
	return stored
	

# def get_flight_history(flight_num):
# 	base = "https://flightaware.com/live/flight/"
# 	end = "/history"
# 	url = base + flight_num + end
# 	page = requests.get(url)
# 	doc = html.fromstring(page.content)
# 	new_releases = doc.xpath("//tr/td[7]/text()")

#SO can also scrape delays from the flightaware specific date time flight link

browser = RoboBrowser(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36')
login()
all_carrier_data = ***REMOVED******REMOVED***
for c in carriers:
	cdata = get_carrier_cancellation_stats(c)
	all_carrier_data[c] = cdata
	print(cdata)

print(all_carrier_data)



