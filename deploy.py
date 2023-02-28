from solcx import compile_standard, install_solc
import json
from web3 import Web3

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
chain_id = 5777

my_address = "0xDd2a8290fEc9dFD0c2b98841D1AAFcdA3B85B8F9"
private_key = "0xc1b750e20006223a7d690166cfa42c46470844e9b34638096edc8e61bfb2"


SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)
# print(SimpleStorage)

#get latest Transaction
nonce = w3.eth.get_transaction_count(my_address)
print(nonce)

#1. Build a Transaction
#2. Sign a Transaction
#3. Send a Transaction

transaction = SimpleStorage.constructor().build_transaction(
    {"gasPrice":w3.eth.gas_price,"chainID":chain_id,"from":my_address,"nonce":nonce}
)
# print(transaction)

signed_txn = w3.eth.account.sign_transaction(transaction,private_key)


# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
