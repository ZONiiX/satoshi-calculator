import requests
import json


url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
usd_rate_dontuse = parsed["bpi"]["USD"]["rate"]
eur_rate_dontuse = parsed["bpi"]["EUR"]["rate"]

doAgain = "y"

while(doAgain == "y"):

    choice1 = input("Do you want to convert to USD or EUR: ")

    #usd code
    if choice1.upper() == "USD":
        usd_rate = float(usd_rate_dontuse.replace(',', ''))
        satoshiUSD = format(usd_rate/100000000, '.8f')

        print('=======SATOSHI/USD=======')
        print('      ', satoshiUSD)
        print("")
        print('=======BITCOIN/USD=======')
        print('      ', usd_rate)
        print("")

        satoshiPriceUserInput = int(input("How much is each coin worth in Satoshi: "))
        satoshiAmountUserInput = int(input("How many coins do you have: "))

        finalSatoshi = satoshiPriceUserInput * usd_rate/100000000
        calculatedAmount = format(satoshiAmountUserInput * finalSatoshi, '.2f')

        print("$", calculatedAmount)
    #eur code
    elif choice1.upper() == "EUR":
        eur_rate = float(eur_rate_dontuse.replace(',', ''))
        satoshiEUR = format(eur_rate/100000000, '.8f')


        print('=======SATOSHI/EUR=======')
        print('      ', satoshiEUR)
        print("")

        print('======BITCOIN/EUR=======')
        print('      ', eur_rate)
        print("")

        satoshiPriceUserInput = int(input("How much is each coin worth in Satoshi: "))
        satoshiAmountUserInput = int(input("How many coins do you have: "))

        finalSatoshi = satoshiPriceUserInput * eur_rate/100000000
        calculatedAmount = format(satoshiAmountUserInput * finalSatoshi, '.2f')

        print("€", calculatedAmount)

    else:
        raise Exception("Enter either USD or EUR")

    print("Do you want to convert again? (y/n)")
    doAgain = input()
