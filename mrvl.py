import hashlib 
import time   
import pandas as pd
from pandas import json_normalize
import json  
import requests #This is used to request information from the API

m = hashlib.md5()   

ts = str(time.time()) 
ts_byte = bytes(ts, 'utf-8') 
m.update(ts_byte) 
m.update(b"4794a03e68692f8ac559cdc0493ec9d1e731d208") #I add the private key to 
    #the hash.Notice I added the b in front of the string to convert it to byte 
    #format, which is required for md5
m.update(b"156ba306ea6a5ac25e219cda7706429d") #And now I add my public key to 
    #the hash
hasht = m.hexdigest()    
#constructing the query
base_url = "https://gateway.marvel.com"  #provided in Marvel API documentation
api_key = "156ba306ea6a5ac25e219cda7706429d" #My public key
query = "/v1/public/characters" +"?"  

#Building the actual query from the information above
query_url = base_url + query +"ts=" + ts+ "&apikey=" + api_key + "&hash=" + hasht
print(query_url) 

#Filtering out query
# https://gateway.marvel.com/v1/public/characters?ts=1665415321.6469138&apikey=156ba306ea6a5ac25e219cda7706429d&hash=5979fd31a609e3101bc3c84b425ccacc&nameStartsWith=Spider&limit=99
# startswith_charac = input("Enter string/character to find")
# limit = input("Enter a number between 0 to 100: ")

# new_query_url = query_url +"&nameStartsWith="+startswith_charac+"&limit="+limit
# print(new_query_url)


#Making the API request and receiving info back as a json
data = requests.get(query_url).json()
print(type(data))
# print(data["data"])
print(data["data"]["results"][0]["resourceURI"])
# count =0
# for i in data["data"]["results"]:
#     print(i)
#     count+=1
#     if count==5:
#         break
df = pd.DataFrame(columns=[data["data"]["results"][0]["resourceURI"],data["data"]["results"][0]["name"]])

for i in range(0,len(data)):
    df.loc = [data["data"]["results"][0]["resourceURI"],data["data"]["results"][0]["name"]]

# for i in range(5):
#     print(data[i])
# print(data)