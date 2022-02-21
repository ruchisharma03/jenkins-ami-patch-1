
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
from os import getenv

load_dotenv()

url = f'https://{getenv("DOMAIN")}.atlassian.net/rest/api/3/issue'

auth = HTTPBasicAuth(getenv('USERNAME'), getenv('API_TOKEN'))

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps({
    "fields": {
        "project":
        {
            "key": getenv('PROJECT_KEY'),
        },
        "summary": getenv('SUMMARY'),
        "description": {
          "type": "doc",
          "version": 1,
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": getenv('DESCRIPTION')
                }
              ]
            }
          ]
        },
        "issuetype": {
            "name": getenv('ISSUETYPE')
        }
    }
})

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text),
      sort_keys=True, indent=4, separators=(",", ": ")))
