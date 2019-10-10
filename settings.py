BASE_URL = "https://www.bitmex.com/api/v1/"

INSTANCE_NAME = "WATCHER_NODE"

MARKET_ORDER_BOOK_DATA_NAME = "orderBookL2"

MONGO_DB_URI = "mongodb://root:toor@172.17.0.1:27017/"

REDIS_HOST = "172.17.0.1"
REDIS_PORT = 6379
REDIS_DB = 0

# If this flag is set True, sample_subscriber.py (it does nothing meaningful.) is executed in another thread.
ENABLE_SAMPLE_SUBSCRIBER = True

# Logging to files is not recommended when you run this on Docker.
# By leaving the name empty the program avoids to create log files.
LOG_FILE_NAME = ''
