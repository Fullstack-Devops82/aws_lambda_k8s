import requests

url = 'http://127.0.0.1:8080/api/v1/namespaces/default/pods'
payload = open("displaysecondmessage.json")
headers = {'content-type': 'application/json', 'Accept': 'application/json'}
response = requests.post(url, data=payload, headers=headers)

print ("*** resp = ", response)
