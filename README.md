# Trading-Bot
Buy for a dolla. Sell for 2

Goal : Un robot qui creer des ordres d'achat/vente en fonction d'ue méthode prédefini. 

Site cible : Bitstamp.com

HTTP API et Websocket API documenté ici
https://www.bitstamp.net/api/
Websocket utilise "Pusher" documenté ici
https://pusher.com/docs

 Qu'est ce qui passe à partir de là ? 

Organisation de l'espace de travail. 

   Q:Quel type de fichier je vais coder ? Un fichier javascript vraissemblablement. Peut être plusieurs ? Ca ne devrait pas etre un projet énorme. 

   R: Projet débuté en python. Installer le client python pour bitstamp. cf https://github.com/kmadac/bitstamp-python-client.
   
   Q:Où tourne le robot ? sur mon pc ? Si oui, et que je veux un robot 24/24 il faut l'heberger -> raspberry pi :P Mais on verra ca plus tard. 
   
   R:Et plus tard c'est maintenant. A priori il suffit de faire tourner des fichiers python sur une machine. un OS pour py basic sous linux et on installe python et roule ma poule. 

Premiere ébauche de robot : 
[x]établir une communication basique. 

[]Etoffer les capacité du bestiaux une par une. 

[]Création de test ? (J'ai lu ca dans un bouquin :P ) 

Processus à atteindre : 
Le robot devrait executer les actions suivantes pour compléter un cycle. 
Un ordre est une offre d'achat ou de vente à un prix fixé. 

1- Lire le nombre d'ordre en cours (le nombre de position de trading ouverte par l'utilisateur et en cours). retourne vrai ou faux si nombre d'ordre limite est atteint. On commencera avec 5 ordres. 

2- Création d'un ordre avec options de cloture sur benefice. (J'achete 1 btc à 100€, j'indique le prix auquel je souahite revendre - par example 103€, quand ce prix est atteint, mon btc est revendu. Il faudrat prendre en compte les frais de transaction pour déterminer le breakeven point et ajusté la strategie en fonction de cette valeur) La création d'ordre pourra se faire pour l'achat de BTC, ou pour l'achat d'EURO) 

J'ai du mal à ecrire c'est dingue. 

Voila le gros du truc quoi. Si t'as des questions on se cause. 

EDIT 
Le portage vers un second site d'échange serait un plus. La 2nde cible serait Kraken.com.
Exemple d'api en node js ici 
https://github.com/nothingisdead/npm-kraken-api/blob/master/kraken.js
