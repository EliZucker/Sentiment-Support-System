import publisher
from datetime import datetime

example_date = datetime.now()

# send_customer_message(message, date, post_id, category)
publisher.send_customer_message("Jetblue", "This could be a twitter post text body", example_date, post_id=57)