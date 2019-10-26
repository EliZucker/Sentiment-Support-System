from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from twitterscraper import query_tweets
import datetime
from publisher import g_pub
#from util import setup_credentials
# import subscriber
import time
# import os
# import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

publisher = g_pub()

def tripadvisor_query():
    browser = webdriver.Chrome()
    browser.get("https://www.tripadvisor.com/Airline_Review-d8729099-Reviews-JetBlue#REVIEWS")
    for i in range(5, 175, 5):
        reviews = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "location-review-review-list-parts-SingleReview__reviewContainer--N7DSv"))
        )
        for review in reviews:
            date_string = review.find_element_by_class_name("social-member-event-MemberEventOnObjectBlock__event_type--3njyv").text
            string_array = date_string.split()
            last_bit = string_array[-1]
            if last_bit == "Today":
                date = datetime.datetime.now()
            elif last_bit == "Yesterday":
                date = datetime.datetime.now() - datetime.timedelta(days=1)
            else:
                date = datetime.date(2019, 10, int(last_bit))
            message = review.find_element_by_class_name("common-text-ReadMore__content--2X4LR").text
            publisher.send_customer_message("jetblue_tripadvisor", ***REMOVED***'sentiment': message***REMOVED***, date)
        # for review in reviews:
        #     print(review.find_element_by_tag_name('span').text)
        browser.find_element_by_xpath("//a[@href='/Airline_Review-d8729099-Reviews-or" + str(i) + "-JetBlue']").click()
        browser.refresh()
    browser.close()

tripadvisor_query()

#input starting and ending datetime objects for range and any search terms (as one string). If we wanted
#all jetblue query strings would just be "jetblue" if we wanted cancellations query strings would be
# "jetblue cancel"

def twitter_query(start_date, end_date, query_strings="jetblue"):
    while start_date < end_date:
        start_string = str(start_date.year) + "-" + str(start_date.month) + "-" + str(start_date.day)
        start_date += datetime.timedelta(days=1)
        end_string = str(start_date.year) + "-" + str(start_date.month) + "-" + str(start_date.day)
        print(start_string + " | " + end_string)
        #tweets = query_tweets(query_strings + " until:" + end_string + " since:" + start_string)
        #for tweet in tweets:
        #print(tweets[0].text + " | " + type(tweets[0].timestamp))
            #publisher.send_customer_message(query_strings + "_twitter", ***REMOVED***'sentiment': tweet.text***REMOVED***, tweet.timestamp, post_id=)


#twitter_query(datetime.date(2019,3,30), datetime.date(2019,4,15))

# credential_path = "YHack-2019-a87246a5ff6d.json"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
#
# def callback(message, date):
#     print(message)
#     print(date)
#
# subscriber.make_customer_message_callback(callback)
#
# print('Listening for messages!')
# while True:
#     time.sleep(60)


# from robobrowser import RoboBrowser
# #
# # browser = RoboBrowser(history=True)
# #
# # # enter dates as strings in the form yyyy-mm-dd so March 3rd 2019 would be 2019-03-03
# # def reddit_query():
# #     browser.open('https://www.tripadvisor.com/Airline_Review-d8729099-Reviews-or55-JetBlue#REVIEWS')
# #     reviews = browser.find_all("div", ***REMOVED***"class": "common-text-ReadMore__content--2X4LR"***REMOVED***)
# #     print(reviews)

    # < div
    #
    # class ="common-text-ReadMore__content--2X4LR" style="max-height: initial;" > < q class ="location-review-review-list-parts-ExpandableReview__reviewText--gOmRC" > < span > They were very kind and really punctual.I appreciate that.Boarding was really in order and the flight attendants were top of the line.Only improvement area is the in fly internet.It was really complicated to use it and there were not really clear instructions.But for the < / span > < span > … < / span > < / q > < / div >

# def is_review(tag):
#     return tag["class"] ==


# import time
#

#
# post_query("2019-03-02", "2019-03-03")

# from twitterscraper import query_tweets
#
#
# # All tweets matching either Trump or Clinton will be returned. You will get at
# # least 10 results within the minimal possible time/number of requests
# for tweet in query_tweets("Trump", 1)[:1]:
#     print(tweet.user.encode('utf-8'))