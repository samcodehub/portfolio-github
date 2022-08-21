import cryptocompare 
btc = cryptocompare.get_price('BTC')
print(btc)

doge = cryptocompare.get_price('DOGE')
print(doge)

btc_usd = cryptocompare.get_price('BTC', currency='USD')
print(btc_usd)