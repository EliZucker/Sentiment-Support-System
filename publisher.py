from google.cloud import pubsub_v1
from datetime import datetime
import json
from util import setup_credentials

project_id = "yhack-2019-257102"
topic_name = "customer-posts"


class g_pub:
    def __init__(self):
        setup_credentials()
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(project_id, topic_name)

    def send_customer_message(self, category, data: dict, date, post_id: str = ''):
        date_string = date.strftime("%m/%d/%Y, %H:%M:%S")
        # Data must be a bytestring
        data = json.dumps(data).encode('utf-8')
        # Add date attribute to the message and publish
        post_id_as_string = post_id.encode("utf-8")
        print('publishing message', data)
        self.publisher.publish(
            self.topic_path, data, date=date_string, post_id=post_id_as_string, category=category,
        )


if __name__ == "__main__":
    publisher = g_pub()
    publisher.send_customer_message('jetblue_twitter',
                                    ***REMOVED***'sentiment': 'i hate jetblue', 'demographic': 'fucker'***REMOVED***,
                                    datetime.now(),
                                    post_id='id 2')

