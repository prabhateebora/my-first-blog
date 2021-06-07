import requests
import json
import urllib.parse 
import urllib.request 



URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id =None):
    data = {}
    if id is not None:
        data = {'id' : id}

    json_data = json.dumps(data)
    headers ={'Content-Type': 'application/json'}
    response = requests.get(url= URL ,headers = headers ,data = json_data )    
    data = response.json()
    print(data)
    

#get_data()    

def post_data():
    data = { 

     
    'name' : 'pohit', 
    'roll' :110, 
    'city' :' nlp'
    }
    json_data = json.dumps(data)
    headers ={'Content-Type': 'application/json'}
    response = requests.post(url= URL ,headers = headers ,data = json_data )  
    data = response.json()
    print(data)

#post_data()



def update_data():
    data = { 

    'id':4, 
    'name' : 'rahul', 
    'roll' :103, 
    'city' :'dhanbad'
    }
    json_data = json.dumps(data)
    headers ={'Content-Type': 'application/json'}
    response = requests.put(url = URL, headers = headers ,data=json_data)
    data = response.json()
    print(data)

#update_data()

def delete_data():
    data = {'id' : 8}
    json_data = json.dumps(data)
    headers ={'Content-Type': 'application/json'}
    response = requests.delete(url = URL, headers = headers ,data=json_data)
    data =response.json()
    print(data)


delete_data()    




