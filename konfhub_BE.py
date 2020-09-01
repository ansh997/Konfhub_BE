import requests
from pprint import pprint

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
bloc=[]
bloc+=response.json()['paid']
bloc+=response.json()['free']
SSconf=[]
for conf in bloc:
  # i, j, k, l, m='confStartDate', 'city', 'venue', 'entryType', 'confUrl'
  if(bloc.count(conf['confUrl'])>1):
    # print(conf['confName'])
    SSconf.append(conf['confName'])

print(SSconf if len(SSconf)!=0 else "No such conferences.")




