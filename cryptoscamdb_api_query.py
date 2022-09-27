import json
import requests
import pandas as pd

solditems = requests.get('https://api.cryptoscamdb.org/v1/whitelist') # (your url)
data = solditems.json()
with open('./Whitelisted domains by CryptoScamDB/whitelisted-domain.json', 'w') as f:
    json.dump(data, f)

df = pd.read_json ('data.json')
df.to_csv ('./Whitelisted domains by CryptoScamDB/whitelisted-domain.csv', index = None)