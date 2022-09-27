import json
import requests
import pandas as pd

url = requests.get('https://api.chainabuse.com/v0/reports?chain=ETH&category=UKRANIAN_DONATION_SCAM&orderByDirection=ASC&orderByField=CREATED_AT&page=1&perPage=50', auth=('ca_NlRJQ1FJWVFzMTNGNm14UVhiUm9Uemc2LmRFOE9acllKMlJaVGdKYzFPc3lQT0E9PQ', '')) # (your url)
data = url.json()
with open('./Ukranian Donation Scam (ChainAbuse)/donation-scam.json', 'w') as f:
    json.dump(data, f)

df = pd.read_json ('./Ukranian Donation Scam (ChainAbuse)/donation-scam.json')
df.to_csv ('./Ukranian Donation Scam (ChainAbuse)/donation-scam.csv', index = None)