import datetime

class Utils:
 def get_actual_timestamp():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return timestamp
