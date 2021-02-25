import json

import requests
from requests.auth import HTTPBasicAuth

url = "https://yossi-nati.atlassian.net/rest/api/2/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "fields": {
        "project":
            {
                "key": "API"
            },
        "summary": "new",
        "description": "Creating of an issue using project keys and issue type names using the REST API",
        "issuetype": {
            "name": "Task"
        }
    }
}

response = requests.post(url, data=json.dumps(payload),
                         auth=HTTPBasicAuth("yossiheftler@gmail.com", "qza7dTiP7bPhzljdRYHb7778"), headers=headers)

print(response.text)
