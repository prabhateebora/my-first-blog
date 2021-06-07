import requests
import json
import urllib.parse 
import urllib.request 




URL = "http://127.0.0.1:8000/stucreate/"

data = {

'id':6,
'name' : 'manu',
'roll' :  106,
'city' : 'kerala',


}

json_data = json.dumps(data)


response = requests.post(url = URL, data=json_data)

data = response.json()

print(data) 

#print(response)

#try:
    #data = response.json()
#except ValueError:
    #print("Response content is not valid JSON")


 










