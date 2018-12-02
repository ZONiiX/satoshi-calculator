import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
usd_rate_dontuse = parsed["bpi"]["USD"]["rate"]
eur_rate_dontuse = parsed["bpi"]["EUR"]["rate"]



#usd code
choice1 = input("Do you want to convert ot USD or EUR: ")

if choice1.upper == "USD":
    usd_rate = float(usd_rate_dontuse.replace(',', ''))
    satoshiUSD = format(usd_rate/100000000, '.8f')

    print('=======SATOSHI/USD=======')
    print('      ',satoshiUSD)
    print("")
    print('=======BITCOIN/USD=======')
    print('      ',usd_rate)
    print("")

#eur code
elif choice1.upper == "EUR":
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


satoshiConversionQuestion = str(input("Do you want to convert to USD or EUR: "))

if satoshiConversionQuestion.upper() == "USD":
    calculatedAmount = float(satoshiUSD) * float(input("Enter satoshi: "))

elif satoshiConversionQuestion.upper() == "EUR":
    calculatedAmount = float(satoshiEUR) * float(input("Enter satoshi: "))

print(calculatedAmount)
