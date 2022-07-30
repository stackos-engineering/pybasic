from time import sleep
import requests

print("Starting example python program")

while True:
    btcprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()
    print(btcprice)
    sleep(10)
