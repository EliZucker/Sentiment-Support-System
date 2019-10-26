from twitterscraper import query_tweets
import datetime
import publisher
from util import setup_credentials
import subscriber
import time
import os
import re
from robobrowser import RoboBrowser

browser = RoboBrowser(history=True)

# enter dates as strings in the form yyyy-mm-dd so March 3rd 2019 would be 2019-03-03
def post_query(start_date, end_date):
    browser.open('https://twitter.com/search?q=jetblue%20until%3A' + start_date +
                 '%20since%3A' + end_date + '&src=typedquery&f=live')

setup_credentials()

#input starting and ending datetime objects for range and any search terms (as one string). If we wanted
#all jetblue query strings would just be "jetblue" if we wanted cancellations query strings would be
# "jetblue cancel"
def post_query(start_date, end_date, query_strings="jetblue"):
    while start_date != end_date:
        start_string = str(start_date.year) + "-" + str(start_date.month) + "-" + str(start_date.day)
        start_date += datetime.timedelta(days=1)
        end_string = str(start_date.year) + "-" + str(start_date.month) + "-" + str(start_date.day)
        tweets = query_tweets(query_strings + " until:" + end_string + " since:" + start_string)
        for tweet in tweets:
            publisher.send_customer_message(tweet.id, tweet.text, tweet.timestamp)


post_query(datetime.date(2019,3,2), datetime.date(2019,3,3))

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



# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
#
#     # while no_of_pagedowns:
#     #     elem.send_keys(Keys.PAGE_DOWN)
#     #     time.sleep(0.2)
#     #     no_of_pagedowns-=1
#
#     # post_elems = browser.find_elements_by_class_name("css-1dbjc4n r-1ila09b r-qklmqi r-1adg3ll")
#     #
#     # for post in post_elems:
#     #     print(post.text)
#
# post_query("2019-03-02", "2019-03-03")

# from twitterscraper import query_tweets
#
#
# # All tweets matching either Trump or Clinton will be returned. You will get at
# # least 10 results within the minimal possible time/number of requests
# for tweet in query_tweets("Trump", 1)[:1]:
#     print(tweet.user.encode('utf-8'))