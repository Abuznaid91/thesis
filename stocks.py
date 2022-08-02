from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = 'USCOMP'
source = ''
page_size = 100
next_page = ''

response = intrinio.StockExchangeApi().get_stock_exchange_realtime_prices(identifier, source=source, page_size=page_size, next_page=next_page)
print(response)