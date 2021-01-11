import requests
import json
def getMyIP():
    url='http://ip-api.com/json/'
    response = requests.get(url)
    data = json.loads(response.content)
    current_ip=data['query']
    #print(data)
    #print (response.status_code)
    return current_ip