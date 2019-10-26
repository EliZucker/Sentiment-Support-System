import subscriber
from datetime import datetime
import time

def callback(message, date, post_id, category):
    print(category)
    print(message)
    print(date)
    print(post_id)
    
subscriber.make_customer_message_callback(callback)

# The subscriber is non-blocking. We must keep the main thread from
# exiting to allow it to process messages asynchronously in the background.
print('Listening for messages!')
while True:
    time.sleep(60)
