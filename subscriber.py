import time
from datetime import datetime
from google.cloud import pubsub_v1

project_id = "yhack-2019-257102"
subscription_name = "customer-posts-sub"

def make_customer_message_callback(callback):
    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/***REMOVED***project_id***REMOVED***/subscriptions/***REMOVED***subscription_name***REMOVED***`
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    def intermediate_callback(message):
        extracted_message = message.data.decode("utf-8")
        extracted_date = datetime.strptime(message.attributes['date'], "%m/%d/%Y, %H:%M:%S")
        message.ack()
        callback(extracted_message, extracted_date)
    
    subscriber.subscribe(subscription_path, callback=intermediate_callback)