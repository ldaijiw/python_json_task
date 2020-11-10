import json

filename = "exchange_rates.json"

def openjson(filename):
    # open jsonfile in read format and return dictionary
    with open(filename, "r") as jsonfile:
        dict_from_json = json.load(jsonfile)
    return dict_from_json

def main():
    exchange_dict = openjson(filename)
    
    base_currency = exchange_dict["base"]
    exchange_rates = exchange_dict["rates"]
    
    # iterate through each exchange rate and print
    for country, rate in exchange_rates.items():
        print(f"\nCOUNTRY: {country}, RATE: {rate}")



if __name__ == "__main__":
    main()