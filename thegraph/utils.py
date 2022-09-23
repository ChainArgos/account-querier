import requests
import csv

thegraphApikey = "ae8a0f25ad5aa5ebe3547ae78f45e347"

class thegraphId :
    aave = "84CvqQHYhydZzr2KSth8s1AFYpBRzUbVJXq6PWuZm9U9"
    kashi = "5mqK2me3PVLTUhMNESgAqq3SX26eGsMFwo8BLLZwNM4u"
    compound = "6tGbL7WBx287EZwGUvvcQdL6m67JGMJrma3JSTtt5SV7"
    euler = "8cLf29KxAedWLVaEqjV8qKomdwwXQxjptBZFrqWNH5u2"
    cream = "9LxWj6eHov86sEJ9Z5XWvanuU3qn992LDwpZf4bace8g"
    curve = "4yx4rR6Kf8WH4RJPGhLSHojUxJzRWgEZb51iTran1sEG"
    uniswapV3 = "EN9rjKtzNitTEb5hgt8bmiyzzhwBpJrJaRihkg8Me8Rr"
    uniswapV2 = "2szAn45skWZFLPUbxFEtjiEzT1FMW8Ff5ReUPbZbQxtt"

def runQuery(query:str, graphId:str):
    request = requests.post(f'https://gateway.thegraph.com/api/{thegraphApikey}/subgraphs/id/{graphId}'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))

def writeOnFile(fileName:str, data:any, fieldnames:list[str]) : 
    with open(f'{fileName}.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writer = csv.writer(f, delimiter = ',')
        writer.writerows(data)