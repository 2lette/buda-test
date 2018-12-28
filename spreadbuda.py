

import json
import requests
import math 

cripto_pares = ["btc-clp", "eth-clp", "ltc-clp", "bch-clp"] # pares disponibles en CLP 

for pair in cripto_pares:
    url = "https://www.buda.com/api/v2/markets/{}/ticker".format(pair)
    r = requests.get(url)

    max_bid = ""
    min_ask = ""
    if r.status_code == 200:
        data = r.json()
        max_bid = float(data["ticker"]["max_bid"][0])
        min_ask = float(data["ticker"]["min_ask"][0])
    else:
        raise Exception(str(r.status_code) + ". Error")

    print "-"*50
    print "Mercado: ", pair.upper()
    print "Maxima Orden de Compra = ", max_bid
    print "Minima Orden de Compra = ", min_ask
    print "Spread = ", min_ask - max_bid
    print "Spread (%) = " , ((min_ask - max_bid)*100)/((max_bid + min_ask)/2)




