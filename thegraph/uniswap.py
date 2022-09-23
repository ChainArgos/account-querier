import time
from utils import thegraphId, runQuery, writeOnFile

def countLiquidityPositions (position) :
    activePosition = [v for v in position['liquidityPositions'] if v['liquidityTokenBalance'] != '0']
    return {'id': position['id'], 'activePostion': len(activePosition)}

# config
skip = 0
first = 1000

while 1 :
  query = f"""
  {{
      users(skip: {skip}, first: {first}) {{
          id
          liquidityPositions {{
            liquidityTokenBalance
          }}
      }}
  }}
  """

  result = runQuery(query, thegraphId.uniswapV2)
  print(f'last skip {skip}')
  skip = skip + first
  
  if(len(result['data']['users']) == 0): 
    break
  filtered = list(map(countLiquidityPositions, result['data']['users']))

  writeOnFile('uniswap-account', filtered,['id', 'activePostion'])

  time.sleep(2)
