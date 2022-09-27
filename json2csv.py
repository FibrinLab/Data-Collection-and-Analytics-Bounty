import pandas as pd

with open('./Blacklisted Domains (Scam Sniffer)/domains.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('./Blacklisted Domains (Scam Sniffer)/domains.csv', encoding='utf-8', index=False)