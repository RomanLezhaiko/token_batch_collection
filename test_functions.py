import os
import json
import time

from web3 import Web3

from functions import *

node_rpc = 'https://data-seed-prebsc-1-s1.binance.org:8545'
web3 = Web3(Web3.HTTPProvider(node_rpc))
print(f"Is connected: {web3.is_connected()}")


with open('/home/roman/Roma/token_batch_collection/wallets.json', '+r') as f:
    wallets = json.load(f)

for wallet in wallets:
    print(get_balance(web3, wallet['public_key']), 'BNB')


# It's work
# txn_hash = make_transaction_main_token(web3, wallets[0]['public_key'], wallets[0]['private_key'], wallets[2]['public_key'], 0.005)
# print(type(txn_hash))
# time.sleep(10)
# txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
# print(txn_receipt)

# It's work
# txn_hash = make_transaction_send_all_main_token(web3, wallets[4]['public_key'], wallets[4]['private_key'], wallets[0]['public_key'])
# time.sleep(10)
# txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
# print(txn_receipt['status'])

# It's work
wallets_list = [wallets[1]['public_key'], wallets[2]['public_key'], 
                wallets[3]['public_key'], wallets[4]['public_key'],
                wallets[5]['public_key'], wallets[6]['public_key'], 
                wallets[7]['public_key'], wallets[8]['public_key']]
txn_hashs = make_transaction_multiple_send_main_token(web3, wallets[0]['public_key'], wallets[0]['private_key'], wallets_list, 0.01)

for txn_hash in txn_hashs:
    txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
    print(txn_receipt['from'], txn_receipt['to'], txn_receipt['status'], sep='   ')



# contract_abi = '[{"inputs":[{"internalType":"uint256","name":"_initialAmount","type":"uint256"},{"internalType":"string","name":"_tokenName","type":"string"},{"internalType":"uint8","name":"_decimalUnits","type":"uint8"},{"internalType":"string","name":"_tokenSymbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":false,"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"allocateTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
# usdt_contract_address = '0xA11c8D9DC9b66E209Ef60F0C8D969D3CD988782c'

# usdt_contract = web3.eth.contract(usdt_contract_address, abi=contract_abi)
# all_functions = usdt_contract.all_functions()
# for func in all_functions:
#     print(func)