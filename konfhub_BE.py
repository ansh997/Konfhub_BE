import requests
from pprint import pprint
import itertools

conferences=[]
duplicates=[]

def printConf(obj):
  for i in set(obj):
    pprint(i)

def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''    
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            duplicates.append(elem)
            return True
    return False

parameters = ['confName', 'confStartDate', 'city', 'venue', 'entryType', 'confUrl']

conferences=[]
url="https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"
response = requests.get(url)
# print(response.json()['free'][0])

for obj in response.json()['free']:
  s=" ".join(obj[i] for i in parameters)
  conferences.append(s)
for obj in response.json()['paid']:
  s=" ".join(obj[i] for i in parameters)
  conferences.append(s)

printConf(conferences)

# check for duplicates
checkIfDuplicates(conferences)
print('#'*89)
print("Duplicates: ", duplicates)

print('#'*89)
print('printing semantically similar conferences.....')

import pandas as pd
df_free=pd.DataFrame(response.json()['free'])
df_paid=pd.DataFrame(response.json()['paid'])
df=pd.concat([df_free, df_paid])
# can upd8 the groupby fields as per requirement
grouped_df=df.groupby(['city'], as_index=False) 
#df.groupby(['city', 'venue'])
for name_of_the_group, group in grouped_df:
   pprint (name_of_the_group)
   pprint (group['confName'])
   print('\n')
