import requests
import csv
import numpy
import time
from utils import thegraphId, runQuery, writeOnFile

# config
skip = 0
first = 1000

while 1 :
  query = f"""
  {{
      accounts(skip: {skip}, first: {first}) {{
          id
      }}
  }}
  """

  result = runQuery(query, thegraphId.curve)
  print(f'last skip {skip}')
  skip = skip + first
  
  if(len(result['data']['accounts']) == 0): 
    break

  writeOnFile('curve-account',result['data']['accounts'],['id'])

  time.sleep(1)

