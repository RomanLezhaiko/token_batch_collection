import os
import json
import time
import logging

from web3 import Web3
from dotenv import load_dotenv

from functions import *


load_dotenv()

node_rpc = os.getenv('NODERPC')
file_path = os.getenv('WALLETS_FILE_PATH')
main_wallet = os.getenv('MAIN_WALLET')
amount_on_balance = float(os.getenv('AMOUNT_ON_BALANCE'))
native_token = os.getenv('NATIVE_TOKEN')

current_dir = os.getcwd()
log_path_directory = os.path.join(current_dir, file_path, 'logs')
if not os.path.exists(log_path_directory):
    os.mkdir(log_path_directory)

log_path = os.path.join(log_path_directory, 'wallets_batch_collection_log.log')
logging.basicConfig(level=logging.INFO, filename=log_path, format='%(asctime)s %(levelname)s %(message)s')

web3 = Web3(Web3.HTTPProvider(node_rpc))
# print(f"Is connected: {web3.is_connected()}")
logging.info(f'Web3 is connected: {web3.is_connected()}')

while True:
    current_dir = os.getcwd()
    file_list = os.listdir(file_path)

    wallets = []
    for file in file_list:
        full_path = os.path.join(current_dir, file_path, file)
        if os.path.isfile(full_path):
            with open(full_path, "+r") as f:
                wallets_tmp = json.load(f)
                for wallet in wallets_tmp:
                    wallets.append(wallet)

    txn_hashs = []
    for wallet in wallets:
        amount = float(get_balance(web3, wallet['public_key'])) - amount_on_balance
        if amount > 0.001:
            txn_hash = make_transaction_main_token(web3, wallet['public_key'], wallet['private_key'], main_wallet, amount)
            txn_hashs.append(txn_hash)
            logging.info(f"Send from {wallet['public_key']} to {main_wallet} amount {amount} {native_token}")

    if len(txn_hashs) > 0:
        time.sleep(15)  
        
        txn_receipt_list = []
        for txn_hash in txn_hashs:   
            txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
            txn_receipt_list.append(txn_receipt) 
            
        for txn_receipt in txn_receipt_list:
            # print(txn_receipt['from'], txn_receipt['to'], txn_receipt['status'], sep='   ')
            logging.info(f"Send from {txn_receipt['from']} to {txn_receipt['to']} with status {txn_receipt['status']}")
            
        # print('All wallets complete.')
        logging.info('All wallets complete.')
    else:
        logging.info('Waiting 1 minute.')
        time.sleep(60)
        