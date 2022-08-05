import requests
import json
url = "https://data.mongodb-api.com/app/data-fqnhr/endpoint/data/beta/action/findOne"
payload = json.dumps({
    "collection": "books",
    "database": "sample_training",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': '<API_KEY>'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)