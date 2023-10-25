import os
import json

file_path = 'wallets/roma'
current_dir = os.getcwd()
file_list = os.listdir(file_path)

wallets = []
for file in file_list:
    full_path = os.path.join(current_dir, file_path, file)
    with open(full_path, "+r") as f:
        wallets_tmp = json.load(f)
        
        for wallet in wallets_tmp:
            wallets.append(wallet)

print(wallets)