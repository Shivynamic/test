import hashlib
import time
import warnings
warnings.filterwarnings("ignore",category=FutureWarning)
import json
import requests
from extractkeys import Private_key,Public_key
import pandas as pd
import response

timestamp = time.time()

def hashing():
    md5hash = hashlib.md5()
    md5hash.update(f'{timestamp}{Private_key}{Public_key}'.encode('utf-8'))
    hashedparam = md5hash.hexdigest()

    return hashedparam


def newfunc(key_api,hash,name_strats_with = None):
     if not key_api and not hash:
         raise AttributeError("Missing API key and Hash Value!")
     elif not key_api:
         raise AttributeError("Missing API Value")
     elif not hash:
         raise AttributeError("Missing hash Value")
#      print(response.raise_for_status())
     timestamp1 = time.time()
     df = pd.DataFrame()

     for i in range(3):
         headers2= {'ts':timestamp1,'apikey':Public_key,'hash':hashing(),'limit':100,'nameStartsWith':name_strats_with,'offset':100*i}
         req2 = requests.get('https://gateway.marvel.com/v1/public/characters',params=headers2,verify=False).json()
         data = req2['data']['results']
         df2 = pd.json_normalize(data)
         df = df.append(df2,ignore_index=True)

     return df[['name','events.available','series.available','stories.available','comics.available','id']]


def filter_character(dataframe , column_name , filter_condition, filter_value):
     if column_name == 'name':
        filter_condition ='starts_with'
        length = len(filter_value)
        return(dataframe[dataframe.name.str[:length]== filter_value])
     else:
        if filter_condition == 'equal_to':
            return(dataframe[dataframe[column_name] == int(filter_value)])
        elif filter_condition == 'less_than':
            return(dataframe[dataframe[column_name] < int(filter_value)])
        elif filter_condition == 'greater_than':
            return(dataframe[dataframe[column_name] > int(filter_value)])
        else:
            return('ERROR - Not a valid filter condition')