import json
import requests
import pandas as pd

solditems = requests.get('https://api.cryptoscamdb.org/v1/scams') # (your url)
data = solditems.json()
with open('./Scams Tracked by CryptoScamDB/cryptobd-tracked-scams.json', 'w') as f:
    json.dump(data, f)

df = pd.read_json ('data.json')
df.to_csv ('./Scams Tracked by CryptoScamDB/cryptobd-tracked-scams.csv', index = None)