from duneanalytics import DuneAnalytics
import pandas as pd
import unicodecsv as csv
import os
from dotenv import load_dotenv

load_dotenv()

userN = os.getenv("USERNAME")
passW = os.getenv("PASSWORD")

# initialize client
# dune = DuneAnalytics('{userN}', '{passW}')
dune = DuneAnalytics('docakan', 'eaglepass225')

# try to login
dune.login()

# fetch token
dune.fetch_auth_token()

result_id = dune.query_result_id(query_id=1319484)

# fetch query result
data = dune.query_result(result_id)

data = data['data']
columns = data['query_results'][0]['columns']
data = data['get_result_by_result_id']

df = pd.DataFrame(data)
df = df['data']
data = df.to_dict()
data = data.values()
print(data)



with open('test.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, columns)
    dict_writer.writeheader()
    dict_writer.writerows(data)