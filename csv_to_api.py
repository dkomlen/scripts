from time import sleep
import requests
import pandas as pd

# Reads data from CSV file and submits it to HTTP API
# Results of the are written in output CSV file

df = pd.read_csv('data.csv', converters={'name': lambda x: str(x)})
df.dropna(inplace=True, how='all')

URL = 'https://...'
HEADERS = {'Authorization': 'Token ...'}
DELAY = 1
responses = []

for index, row in df.iterrows():
    sleep(DELAY)

    # skip empty rows
    if row['test'] == '':
        continue

    data = {'name': row['Name'].strip()}
    print(data)
    response = requests.post(URL, data = data, headers = HEADERS)
    print(response.text)
    responses.append((row['id'], response.json().get('id', 'N/A'), response.json()['status']))

res = pd.DataFrame(responses, columns=['row_id', 'response_id', 'status'])
res.to_csv('results.csv')