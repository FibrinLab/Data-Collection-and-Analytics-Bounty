import json
import requests
import pandas as pd

url = requests.get('https://api.chainabuse.com/v0/reports?chain=ETH&category=RANSOMWARE&orderByDirection=ASC&orderByField=CREATED_AT&page=1&perPage=50', auth=('ca_NlRJQ1FJWVFzMTNGNm14UVhiUm9Uemc2LmRFOE9acllKMlJaVGdKYzFPc3lQT0E9PQ', '')) # (your url)
data = url.json()
with open('./Ransomware (ChainAbuse)/ransomware.json', 'w') as f:
    json.dump(data, f)

df = pd.read_json ('./Ransomware (ChainAbuse)/ransomware.json')
df.to_csv ('./Ransomware (ChainAbuse)/ransomware.csv', index = None)