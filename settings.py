SYMBOL                          = "XBTUSD"
INSTANCE_NAME                   = "WATCHER_NODE"

REDIS_HOST                      = "dev.huemae.ru"
REDIS_PORT                      = 6379
REDIS_DB                        = 0

BASE_URL                        = "https://www.bitmex.com/api/v1/"
MONGO_DB_URI                    = "mongodb://root:toor@dev.huemae.ru:27017/"

BITMEX_DB                       = "bitmex_data"
TRADES_COLLECTION               = "trades"
TRADES_CURSOR_COLLECTION        = "trades_cursor"
ORDER_BOOK_SNAPSHOTS_COLLECTION = "order_book_snapshots"
ORDER_BOOK_L2_DATA_COLLECTION   = 'orderbook_l2_data'
MARKET_ORDER_BOOK_DATA_NAME     = "orderBookL2"

TARGET_ORDER_BOOK_PRICE_RATIO             = 0.005
LOOP_INTERVAL                             = 1.5
MAX_ORDERS_IDLE_COUNT                     = 5
MAX_TRADES_IDLE_COUNT                     = 25
MAX_TRADES_COLLECTION_BYTES               = 100000000
MAX_ORDER_BOOK_COLLECTION_BYTES           = 100000000

REDIS_ORDER_BOOK_SNAPSHOT_ID_CHANNEL_NAME = 'from-watcher:order-book-snapshot-id'
REDIS_ORDER_BOOK_L2_ID_CHANNEL_NAME       = 'from-watcher:order-book-snapshot-id'
ENABLE_SAMPLE_SUBSCRIBER                  = True
LOG_FILE_NAME                             = ''


