import time
from utils import thegraphId, runQuery, writeOnFile

# config
skip = 0
first = 1000

while 1 :
  # The Graph query - Query aave for a list of the last 10 flash loans by time stamp
  query = f"""
  {{
      accounts(skip: {skip}, first: {first}) {{
          id
          hasBorrowed
      }}
  }}
  """

  result = runQuery(query, thegraphId.cream)
  print(f'last skip {skip}')
  skip = skip + first
  
  if(len(result['data']['accounts']) == 0): 
    break

  writeOnFile('cream-account',result['data']['accounts'],['id', 'hasBorrowed'])

  time.sleep(2)
