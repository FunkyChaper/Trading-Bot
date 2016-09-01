import bitstamp.client
public_client = bitstamp.client.Public()
trader = bitstamp.client.Trading('ID', 'key', 'secret')

import krakenex

## Collectes des infos dont nous allons avoir besoin

#1
############################prix du marché chez kraken
k = krakenex.API()
kTicker = k.query_public('Depth', {'pair': 'XBTCZEUR','count' : '10'})
#print(kTicker.keys())
results = kTicker ['result']
#print (results)
pair_BTC_EUR = results ['XXBTZEUR']
#print (results.keys())
#print (kt.keys())
asks = pair_BTC_EUR ['asks']
bids = pair_BTC_EUR ['bids']
#print (asks)
asks_first_order = asks [0]
bids_first_order = bids [0]
#print (first_order)
asks_market_price_kraken = float(asks_first_order [0])
bids_market_price_kraken = float(bids_first_order [0])


############################prix du marché chez bitstamp

last_orders = trader.order_book() # order_book returns a list (asks and bids) made of list of transaction (price, volume)
order_book_asks = last_orders['asks'][0]
order_books_bids = last_orders['bids'][0]
asks_market_price_bitstamp = float(order_book_asks[0])
bids_market_price_bitstamp = float(order_books_bids[0])

# definir les variables globales qui seront utiliser ds les fnctions 
lowest_asks = 0
highest_bids = 0
buy_exchange = ''
sell_exchange = ''

############################ Calcul de frais de transaction
#	trouver les feees chez kraken.com et bitstamp.net
#fees_bitstamp 0.25%
fees_bitstamp = 0.0025
#fees_kraken : 0.26%
fees_kraken = 0.0026
investement_eur = 100
investement_btc = 1
fees_selector = 0.5
#TODO : utiliser le client API pour obtenir les fees en temps reel. 

##fonction de slelection de fees en rapport avec l'exchange choisi

#Si pas de possibilité d'arbitrage, 
trigger = False

def arbitrage_trigger():
	if highest_bids > lowest_asks :  
		print ('Now would be a good time to buy!!!!!')
		print('Lets buy some BTC for ' + str(investement_eur) + 'EUROS')
		trigger = True
		set_buy_exchange ()	
	else : 
		print ('No arbitrage opportunity...')
		simulation ()


def set_buy_exchange():
	if trigger ==True :
		if (asks_market_price_kraken>asks_market_price_bitstamp):
			lowest_asks = asks_market_price_bitstamp
			buy_exchange = 'Bitstamp'
		else:
			lowest_asks = asks_market_price_kraken
			buy_exchange = 'Kraken'
			
		if (bids_market_price_bitstamp <bids_market_price_kraken):
			highest_bids = bids_market_price_kraken
			sell_exchange = 'Kraken'
		else :
			highest_bids = bids_market_price_bitstamp
			sell_exchange = 'Bitstamp'
	else:
		print ('we pick the lowest ask order from both site, here, ' + str(lowest_asks) + 'at ' + buy_exchange)	
	trigger_buy_order()


lowest_spread = round (float(lowest_asks) - float(highest_bids), 4)

def trigger_buy_order():
	if trigger == True:
		if buy_exchange	!= 'Bitstamp':
			fees_selector = 0.0026
			k.load_key('kraken.key')
			k.query_private('AddOrder', {'pair': 'XXBTZEUR',
	                             'type': 'buy',
	                             'ordertype': 'limit',
	                             'price': str(asks_market_price_kraken),
	                             'volume': str(investement_eur / (1 - fees_selector))})
		else : 
			buy_order_bitstamp = trader.buy_limit_order((investement_eur/(1- fees_selector), lowest_asks))

	else : 
		print ('lets make a simulation')
		if buy_exchange == 'Kraken' : 
			print ('We bought 99.751 EUR of BTC @ ' + str(asks_market_price_kraken) + 'from Kraken')
		else :
			print('We bought 99.751 EUR of BTC @ ' + str(asks_market_price_bitstamp) + 'from Bitstamp') 
	place_matching_sell_order()		

def place_matching_sell_order():
	if trigger == True:
		if sell_exchange !=('Bitstamp'):
			k.load_key('kraken.key')
			k.query_private('AddOrder', {'pair': 'XXBTZEUR',
                             'type': 'sell',
                             'ordertype': 'limit',
                             'price': str (bids_market_price_kraken),
                             'volume': str(investement_eur/(1-fees_selector))})
		else : 
			trader.sell_limit_order(investement_eur, highest_bids)
	else: 
		print ('We now sell that exact same amount of BTC into euros again. ')
		print ('''figures are as such: 
			\n enter the market with 100 euros
			''')
		print ('we receive  ' + str(investement_eur/1-fees_selector) + 'worth of BTC, that is ' + (investement_eur/(1-fees_selector)/bids)
		print ('next we sell at the other exchange')
arbitrage_trigger()
