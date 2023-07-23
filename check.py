import requests
import json
import os

def get_oil_prices():
    API_key = "YOUR_EIA_API_KEY"  # Replace with your EIA API Key
    url = f"http://api.eia.gov/series/?api_key={API_key}&series_id=PET.RBRTE.D"
    response = requests.get(url)
    data = json.loads(response.text)
    series = data['series'][0]['data']
    prices = {item[0]: item[1] for item in series}  # dictionary with date as key and price as value
    return prices

def load_oil_prices(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            prices = json.load(f)
    else:
        prices = {}
    return prices

def update_oil_prices(filename):
    current_prices = get_oil_prices()
    stored_prices = load_oil_prices(filename)
    stored_prices.update(current_prices)  # merge the dictionaries
    with open(filename, 'w') as f:
        json.dump(stored_prices, f)  # write the updated prices back to the file

def main():
    filename = 'oil_prices.json'
    update_oil_prices(filename)
    prices = load_oil_prices(filename)
    for date, price in prices.items():
        print(f"Date: {date}, Price: {price}")

if __name__ == "__main__":
    main()
