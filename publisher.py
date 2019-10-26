from google.cloud import pubsub_v1
import datetime

project_id = "yhack-2019-257102"
topic_name = "customer-posts"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

def send_customer_message(message, date):
    date_string = date.strftime("%m/%d/%Y, %H:%M:%S")
    # Data must be a bytestring
    data = message.encode('utf-8')
    # Add date attribute to the message and publish
    publisher.publish(
        topic_path, data, date=date_string
    )
