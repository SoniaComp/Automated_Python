import requests
import json

with open('./secrets.json', "r") as json_file:
    secrets = json.load(json_file)
    print(secrets)

username = secrets['username']
api_token = secrets['api_token']

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

header = {
    'X-Github-Username': '%s' % username,
    'Content-Type': 'application/json',
    'Authorization': 'token %s' % api_token
}
print(header)


url = "/gists"
data = {
    "description": "the description for this gist",
    "public": "True",
    "files": {
        "file1.txt": {
            "content": "String file contents"
        }
    }
}

r = requests.post('%s%s' % (BASE_URL, url),
                  headers=header, data=json.dumps(data))
print(r.json())
