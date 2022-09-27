import json
import requests
import pandas as pd

solditems = requests.get('https://api.cryptoscamdb.org/v1/scams') # (your url)
data = solditems.json()
with open('data.json', 'w') as f:
    json.dump(data, f)

df = pd.read_json ('data.json')
df.to_csv ('testagain.csv', index = None)