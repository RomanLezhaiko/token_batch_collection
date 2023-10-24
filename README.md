# token_batch_collection

## Quick start

In your command line:
```
git clone https://github.com/RomanLezhaiko/token_batch_collection.git
cd token_batch_collection
```

Create virtual enviroment:
```
python3 -m venv .venv

source .venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

## Run with Docker

In your command line:
```
git clone https://github.com/RomanLezhaiko/token_batch_collection.git
cd token_batch_collection
mkdir -p wallets/your_folder_name
```

In folder wallets/your_folder_name create json file with data like in wallets_example.json
If you need change AMOUNT_ON_BALANCE in Dockerfile.
In docker-compose.yml change WALLETS_FILE_PATH on wallets/your_folder_name, change NODERPC for blockchain that you are use and change MAIN_WALLET that will collect tokens from all wallets. Save all files.


In your command line:
```
docker compose up -d
```