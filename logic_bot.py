import types
import bitstamp.client
#trading strategy :
# On vends des BTC au prix du marché et on place un ordre d'achat à un prix inferieur pour récuperer ses btc et avoir du cash qui reste. 
# exemple 
# qq un veut acheter des BTC à un prix de 100 eur/ BTC. C'est la meilleur offre. C'est le prix du marché. 
# on lui vend des btc (une somme calculé a partir de notre investissement de base)
# 1- Déterminer la taille de l'ordre (1 unité = 1% de balance available)
# 2- Déterminer le prix du marché (orderbook asks )
# 3- Déterminer le taux de commission.
# 4- Déterminer le prix de vente pour 1% de bénéfice net.
# 5- Achat de bitcoin au prix du marché pour un volume de 1 unité. 
# 6- Creation d'un ordre d'achat à prix inferieur
# 7- Laisser le marché bouger. 
# C'est de la loterie. Autant faire un truc fun pour commencer à programmer :P 
# Il reste a implémenter une vrai strategie. Je crois avoir encore pas mal de lecture a faire à ce sujet. 


import bitstamp.client
public_client = bitstamp.client.Public()
trader = bitstamp.client.Trading('08096', 'Q2P7lXiZviLnQYGMQ9HZ9B5nEz2luBCi', 'EU5Nb1jqFLz1j44YIY3xiTQKdCFhn1pU')

# 1
#apelle de la fonction account_balance sur l'objet trader. Obtention d'un dictionnaire de liste
raw_balance = trader.account_balance()
a = float(str(raw_balance ['btc_available']))
unit = a/100
print ('On va dépenser ' + str(unit) + 'BTC')
# 2
public_client = bitstamp.client.Public()
last_orders = trader.order_book() # order_book returns a list (asks and bids) made of list of transaction (price, volume)
order_book_asks = last_orders['asks'][0]
market_price = float(str(order_book_asks[0]))
print ('pour vendre des BTC à ' + str(market_price) + ' EUR/BTC')
# 3 fees is in % so 0.25% per transactions at the start. It goes down according to volume.  
fees = float(str(raw_balance['fee']))
shaved_price = (market_price * (1 - fees/100))
print ('ou encore comission incluse : ' + str(shaved_price) + ' EUR/BTC')
# 4
selling_price = (market_price*(1 - (3* fees/100)))
print ('SI on souhaite marger 3x les fees, on rachete au prix de ' + str(selling_price) + ' Eur/BTC, soit 0,75 pour cent de retour ?.')


