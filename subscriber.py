import time
from datetime import datetime
from google.cloud import pubsub_v1
from util import setup_credentials

project_id = "yhack-2019-257102"
subscription_name = "customer-posts-sub"

# Callback must be in form:
# callback(category, message, date, post_id)
def make_customer_message_callback(callback):
    setup_credentials()
    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/***REMOVED***project_id***REMOVED***/subscriptions/***REMOVED***subscription_name***REMOVED***`
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    def intermediate_callback(message):
        extracted_message = message.data.decode("utf-8")
        extracted_date = datetime.strptime(message.attributes['date'], "%m/%d/%Y, %H:%M:%S")
        extracted_post_id = int(message.attributes['post_id'])
        extracted_category = message.attributes['category']
        message.ack()
        callback(extracted_category, extracted_message, extracted_date, extracted_post_id)
    
    subscriber.subscribe(subscription_path, callback=intermediate_callback)