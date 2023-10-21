import json
import time

from web3 import Web3

from functions import get_balance, make_transaction_main_token, make_transaction_send_all_main_token


rpc_url = "https://data-seed-prebsc-1-s1.binance.org:8545"
web3 = Web3(Web3.HTTPProvider(rpc_url))
print(f"Is connected: {web3.is_connected()}")


with open('/home/roman/Roma/token_batch_collection/wallets.json', "+r") as f:
    wallets = json.load(f)


for wallet in wallets:
    print(get_balance(web3, wallet['public_key']), 'BNB')


# It's work
# txn_hash = make_transaction_main_token(web3, wallets[0]['public_key'], wallets[0]['private_key'], wallets[2]['public_key'], 0.005)
# print(type(txn_hash))
# time.sleep(10)
# txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
# print(txn_receipt)

txn_hash = make_transaction_send_all_main_token(web3, wallets[1]['public_key'], wallets[1]['private_key'], wallets[0]['public_key'])
time.sleep(10)
txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
print(txn_receipt)
