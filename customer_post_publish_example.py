import publisher
from datetime import datetime

example_date = datetime.now()

publisher.send_customer_message("This could be a twitter post text body", example_date)
