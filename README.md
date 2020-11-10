# Python JSON Task

- In this instance we will be using a JSON file with exchange rates and build your class around it.
- You will see from the exchange rates file that you will be accessing these data points as you would in a dictionary.
- Have exchange_rates.json file available 
- Display data from .json file
- iterate through data and display exchange rate by country

**SOLUTION NOTES**
- Information contained in **J**ava**S**cript **O**bject **N**otation format, and has to be converted into a dictionary in Python so that it is accessible
```python
import json

def openjson(filename):
    # open jsonfile in read format and return dictionary
    with open(filename, "r") as jsonfile:
        dict_from_json = json.load(jsonfile)
    return dict_from_json
```
 
```json
{
    "base": "EUR",
    "date": "2017-07-26",
    "rates": {
      "AUD": 1.4717,
      "BGN": 1.9558,
        .
        .
        .
      "ZAR": 15.2
    }
  }
```