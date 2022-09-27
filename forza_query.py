import requests
# pretty print is used to print the output in the console in an easy to read format
from pprint import pprint
import json
import pandas as pd
import csv


query = '''
  query pastAlerts($input: AlertsInput) {
      alerts(input: $input) {
        pageInfo {
          hasNextPage
          endCursor {
            alertId
            blockNumber
          }
        }
        alerts {
          addresses
          projects {
            id
          }
          name
          protocol
          findingType
          source {
            transactionHash
            block {
              number
              timestamp
              chainId
            }
          }
          severity
          metadata
        }
      }
  }
'''

variables = {
  "input": {
      "first": 5,
      "bots": ["0x1d646c4045189991fdfd24a66b192a294158b839a6ec121d740474bdacb3ab23"],
      "chainId": 1,
      "blockSortDirection": "asc",
      "blockDateRange": {
        "startDate": "2022-09-01",
        "endDate": "2022-09-26"
      }
  }
}

request = requests.post('https://api.forta.network/graphql'
                            '',
                            json={'query': query, 'variables': variables})
json_data = json.loads(request.text)

# pprint(json_data)
json_object = json.dumps(json_data, indent=4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)

# # convert json into a dataframe
# df = pd.DataFrame(json_data['data']['pairs'])

# # check result
# pprint(df)

# # writing data to csv
# df.iloc[:,0:4].to_csv("fetchedData.csv", index=False)

# # print the results
# print('Print Result - {}'.format(result))
# print('#############')
# # pretty print the results
# pprint(result)

# Opening JSON file and loading the data
# into the variable data
def read_json(filename: str) -> dict:
  
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")
  
    return data
  
  
def normalize_json(data: dict) -> dict:
  
    new_data = dict()
    for key, value in data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k, v in value.items():
                new_data[key + "_" + k] = v
      
    return new_data

data = read_json(filename="sample.json")
  
    # Normalize the nested python dict 
new_data = normalize_json(data=data)
  
print("New dict:", new_data, "\n")
  
    # Create a pandas dataframe 
dataframe = pd.DataFrame(new_data, index=[0])
  
    # Write to a CSV file
dataframe.to_csv("article.csv")