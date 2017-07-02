import requests
from getpass import getpass
import json

username = ''
password = ''

url = 'https://api.github.com/authorizations'
note = 'Mining git'
postData = {
  'scopes' : 'repo',
  'note' : note
}

response = requests.post(url, auth = (username, password), data = json.dumps(postData))
if response.status_code == requests.codes.ok:
    print 'Error API response: ', response.text

print 'API response: ', response.text
print 'Your Oauth token is', response.json()['token']

