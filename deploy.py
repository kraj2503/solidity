from solcx import compile_standard, install_solc
import json
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

    # print(simple_storage_file)
install_solc("0.6.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"simpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evmsourceMap"]}
            },
        },
    },
    solc_version="0.6.0",
)
# print(compiled_sol)
with open("compiled_code.json","w") as file:
    json.dump(compiled_sol,file)

bytecode = compiled_sol["contracts"]["simpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get ABI
abi = compiled_sol["contracts"]["simpleStorage.sol"]["SimpleStorage"]["abi"]
# print(abi)

#Connecting to Ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337

my_address = "0x6E335E1B6026460e83C4A502dB7bc70798fAD5fe"
private_key = os.getenv("PRIVATE_KEY")


SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)
# print(SimpleStorage)

#get latest Transaction
nonce = w3.eth.get_transaction_count(my_address)
# # print(nonce)

# #1. Build a Transaction
# #2. Sign a Transaction
# #3. Send a Transaction

transaction = SimpleStorage.constructor().build_transaction(
    {"gasPrice":w3.eth.gas_price,"chainId":chain_id,"from":my_address,"nonce":nonce}
)
# # print(transaction)

signed_txn = w3.eth.account.sign_transaction(transaction,private_key=private_key)
# print(signed_txn)

tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_recipt= w3.eth.wait_for_transaction_receipt(tx_hash)

