import pandas as pd
import requests

forta_api = "https://api.forta.network/graphql"
headers = {"content-type": "application/json"}

# start and end date needs to be in the format: YYYY-MM-DD
START_DATE = "2022-04-20"
END_DATE = "2022-04-21"
ALERT_COUNT_LIMIT = 100000

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

query_variables = {
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

all_alerts = []
next_page_exists = True

while next_page_exists and len(all_alerts) < ALERT_COUNT_LIMIT:
    # query Forta API
    payload = dict(query=query, variables=query_variables)
    response = requests.request("POST", forta_api, json=payload, headers=headers)

    # collect alerts
    data = response.json()['data']['alerts']
    alerts = data['alerts']
    all_alerts += alerts

    # get next page of alerts if it exists
    next_page_exists = data['pageInfo']['hasNextPage']
    # endCursor contains alert Id and block number.
    # This is needed to get the next page of alerts.
    end_cursor = data['pageInfo']['endCursor']
    query_variables['input']['after'] = end_cursor

df = pd.DataFrame.from_dict(all_alerts)
print(df)
df.iloc[:,0:4].to_csv("fetchedData.csv", index=False)

len(df) # size: ALERT_COUNT_LIMIT = 100000