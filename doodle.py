# Bitstamp trading bot test

import bitstamp.client

public_client = bitstamp.client.Public()

trader = bitstamp.client.Trading('ID', 'KEY', 'SECRET')
balance = trader.account_balance()
last_orders = public_client.order_book() # order_book returns a list (asks and bids) made of list of transaction (price, volume)
for i in range (0,10):
	print (last_orders['bids'][i])

for i in range (0,10):
	print (last_orders['asks'][i])
print (balance['btc_balance'])