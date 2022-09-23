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
          positionCount
          borrowCount
      }}
  }}
  """

  result = runQuery(query, thegraphId.aave)
  print(f'last skip {skip}')
  skip = skip + first
  
  if(len(result['data']['accounts']) == 0): 
    break

  writeOnFile('aave-account', result['data']['accounts'], ['id', 'positionCount', 'borrowCount'])

  time.sleep(2)
