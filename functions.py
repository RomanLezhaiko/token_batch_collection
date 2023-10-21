from typing import Any

from web3 import Web3


def get_balance(web3: Web3, wallet_address: str) -> int:
    checksum_address = Web3.to_checksum_address(wallet_address)
    balance = web3.eth.get_balance(checksum_address)
    ether_balance = Web3.from_wei(balance, 'ether')
    return ether_balance


def make_transaction_main_token(web3: Web3, from_address: str, private_key: str, to_address: str, amount: float) -> Any:
    '''
    Функция для отправки определенного количества токенов сети
    
    :param web3: Объект web3
    :param from_address: С какого адреса произвести отправку
    :param private_key: Приватный ключ для адреса с которого будет производиться отправка
    :param to_address: На какой адрес будут отправлены монеты
    :param amount: Количество монет для отправки
    '''

  	# цена газа
    gas_price = web3.eth.gas_price
    
    # количество газа
    gas = 2_000_000  # ставим побольше

    # число подтвержденных транзакций отправителя
    nonce = web3.eth.get_transaction_count(from_address)

    txn = {
        'chainId': web3.eth.chain_id,
        'from': from_address,
        'to': to_address,
        'value': int(Web3.to_wei(amount, 'ether')),
        'nonce': nonce, 
        'gasPrice': gas_price,
        'gas': gas,
    }

    signed_txn = web3.eth.account.sign_transaction(txn, private_key)
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
    return txn_hash


def make_transaction_send_all_main_token(web3: Web3, from_address: str, private_key: str, to_address: str) -> Any:
    '''
    Функция для отправки всех монет сети с кошелька
    
    :param web3: Объект web3
    :param from_address: С какого адреса произвести отправку
    :param private_key: Приватный ключ для адреса с которого будет производиться отправка
    :param to_address: На какой адрес будут отправлены монеты
    '''

    balance = web3.eth.get_balance(from_address)
  	# цена газа
    gas_price = web3.eth.gas_price
    
    # количество газа
    gas = 21000
    # balance -= gas
    balance = balance - (gas * gas_price)
    # число подтвержденных транзакций отправителя
    nonce = web3.eth.get_transaction_count(from_address)

    txn = {
        'chainId': web3.eth.chain_id,
        'from': from_address,
        'to': to_address,
        'value': int(balance),
        'nonce': nonce, 
        'gasPrice': gas_price,
        'gas': 0,
    }

    gas_tmp = web3.eth.estimate_gas(txn)
    txn.update({'gas': gas_tmp})
    signed_txn = web3.eth.account.sign_transaction(txn, private_key)    
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
    return txn_hash
