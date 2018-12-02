import requests
import json
import sys


url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
usd_rate_dontuse = parsed["bpi"]["USD"]["rate"]
eur_rate_dontuse = parsed["bpi"]["EUR"]["rate"]

doAgain = "y"

while(doAgain == "y"):

    #usd code
    choice1 = input("Do you want to convert to USD or EUR: ")

    if choice1.upper() == "USD":
        usd_rate = float(usd_rate_dontuse.replace(',', ''))
        satoshiUSD = format(usd_rate/100000000, '.8f')

        print('=======SATOSHI/USD=======')
        print('      ',satoshiUSD)
        print("")
        print('=======BITCOIN/USD=======')
        print('      ',usd_rate)
        print("")

    #eur code
    elif choice1.upper() == "EUR":
        eur_rate = float(eur_rate_dontuse.replace(',', ''))
        satoshiEUR = format(eur_rate/100000000, '.8f')


        print('=======SATOSHI/EUR=======')
        print('      ',satoshiEUR)
        print("")

        print('======BITCOIN/EUR=======')
        print('      ', eur_rate)
        print("")
    else:
        raise Exception("Enter either USD or EUR")


    satoshiPriceUserInput = int(input("How many Satoshi is each coin worth: "))
    satoshiAmountUserInput = int(input("How many coins do you have: "))

    calculatedAmount = satoshiAmountUserInput * satoshiUSD

    print(calculatedAmount*satoshiAmountUserInput)

    print("Do you want to convert again? (y/n)")
    doAgain = input()

    
