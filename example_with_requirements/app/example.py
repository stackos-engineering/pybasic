from time import sleep
import requests

print("Starting example python program")

while True:
    btcprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()
    print(btcprice)
    print("Waiting 60 seconds before update")
    sleep(15)
    print("Waiting 45 seconds before update")
    sleep(15)
    print("Waiting 30 seconds before update")
    sleep(15)
    print("Waiting 15 seconds before update")
    sleep(15)
