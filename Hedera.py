import requests
import time
from TwitterBot import tweet_data


exchange_rate = 0.1175

BASE_URL = 'https://mainnet-public.mirrornode.hedera.com'
current_api_endpoint = '/api/v1/accounts'

def parse_hedera_accounts():
    global current_api_endpoint
    
    while True:
        url = BASE_URL + current_api_endpoint
        response = requests.get(url)
        
        try:
            data = response.json()
        except ValueError:
            print("Failed to parse JSON response:")
            print(response.content)
            continue
        
        for account in data['accounts']:
            bal = account['balance']
            account_balance = bal['balance'] / 100000000
            print('HBAR balance:', account_balance)
            usd_balance = account_balance * exchange_rate
            print('USD balance:', usd_balance)
            
            if usd_balance > 10000:
                evm_add = account['evm_address']
                tweet_data({'evm_address': evm_add, 'usd_balance': usd_balance})

                
        if 'next' not in data['links']:
            break
        
        current_api_endpoint = data['links']['next']
        time.sleep(1800)

parse_hedera_accounts()
