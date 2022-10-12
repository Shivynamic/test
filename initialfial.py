import pandas as pd
import requests
import warnings 
warnings.filterwarnings("ignore",category=FutureWarning)

import time
import hashlib
from extractkeys import Public_key,Private_key

import sys
sys.path.insert(0,'Marvel_Solve/Mod5_act1/M')

address = "https://gateway.marvel.com/v1/public/characters"
ts = str(time.time())
temp =[]
list2pandas =[]

def mdhash(privatekey,publickey,ts):
     strhash = ts+privatekey+publickey
     result = hashlib.md5(strhash.encode())
     return result.hexdigest()



ls = [0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600]

for k in ls:
    paramtrs = dict(apikey =Public_key,ts=ts,hash = mdhash(Private_key,Public_key,ts), offset =k,limit = '100' )
    headers = {'Content-Type':'application/json'}
    response = requests.get(address,params=paramtrs,headers=headers)

    res11 = response.json()
    for i in  res11['data']['results']:
#          temp.extend(i['id'],i['name'],i['comics']['available'],i['series']['available'],i['stories']['available'],i['events']['available'])

         
         temp.append(i['id'])
         temp.append(i['name'])
         temp.append(i['comics']['available'])
         temp.append(i['series']['available'])
         temp.append(i['stories']['available'])
         temp.append(i['events']['available'])
         
         list2pandas.append(temp)
         temp =[]
     
    df = pd.DataFrame(list2pandas,columns=['id','Character_Name','Events','Comics','Series','Stories'])
df.to_csv('characters.csv')
print(df)

