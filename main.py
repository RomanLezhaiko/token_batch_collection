import os
import json
import time

from web3 import Web3
from dotenv import load_dotenv

from functions import *


load_dotenv()

node_rpc = os.getenv('NODERPC')
file_path = os.getenv('WALLETS_FILE_PATH')
main_wallet = os.getenv('MAIN_WALLET')
amount_on_balance = float(os.getenv('AMOUNT_ON_BALANCE'))

web3 = Web3(Web3.HTTPProvider(node_rpc))
print(f"Is connected: {web3.is_connected()}")

while True:
    current_dir = os.getcwd()
    file_list = os.listdir(file_path)

    for file in file_list:
        full_path = os.path.join(current_dir, file_path, file)
        # print(full_path)
        with open(full_path, "+r") as f:
            wallets = json.load(f)

        txn_hashs = []
        for wallet in wallets:
            amount = float(get_balance(web3, wallet['public_key'])) - amount_on_balance
            if amount > 0.001:
                txn_hash = make_transaction_main_token(web3, wallet['public_key'], wallet['private_key'], main_wallet, amount)
                txn_hashs.append(txn_hash)

        time.sleep(15)  
        
        txn_receipt_list = []
        for txn_hash in txn_hashs:   
            txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
            txn_receipt_list.append(txn_receipt) 
        
        for txn_receipt in txn_receipt_list:
            print(txn_receipt['from'], txn_receipt['to'], txn_receipt['status'], sep='   ')
        
        print(f'File {full_path} complete.')

