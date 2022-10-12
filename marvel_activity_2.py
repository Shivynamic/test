import hashlib
import time
import warnings 
warnings.filterwarnings("ignore",category=FutureWarning)

import json
import requests
from extractkeys import Private_key,Public_key
import pandas as pd

timestamp = time.time()

def hashing():
    md5hash = hashlib.md5()
    md5hash.update(f'{timestamp}{Private_key}{Public_key}'.encode('utf-8'))
    hashedparam = md5hash.hexdigest()

    return hashedparam

limit1= input("Provide limit")
name = input("Provide Starting Name ")
headers1= {'ts':timestamp,'apikey':Public_key,'hash':hashing(),'limit':limit1,'nameStartsWith':name}



'''trial begin '''
pq = "https://gateway.marvel.com/v1/public/characters"
base_url = "https://gateway.marvel.com"  #provided in Marvel API documentation
api_key = Public_key #My public key
query = "/v1/public/characters" +"?"  

newt = str(timestamp)
#Building the actual query from the information above
query_url = base_url + query +"ts=" + newt+ "&apikey=" + api_key + "&hash=" + hashing()
'''end '''

# print(query_url) 

req1 = requests.get('https://gateway.marvel.com/v1/public/characters',params=headers1,verify=False).json()
data = req1['data']['results']

df1 = pd.json_normalize(data)

df1[['name','events.available','series.available','stories.available','comics.available','id']]

print("dynamic",df1)



df11 = pd.DataFrame()

for i in range(3):
    headers2= {'ts':timestamp,'apikey':Public_key,'hash':hashing(),'limit':100,'offset':100*i}
    req2 = requests.get('https://gateway.marvel.com/v1/public/characters',params=headers2,verify=False).json()
    data = req2['data']['results']
    df2 = pd.json_normalize(data)
    df11 = df11.append(df2,ignore_index=True)

newd =df11[['name','events.available','series.available','stories.available','comics.available','id']]
print(newd)