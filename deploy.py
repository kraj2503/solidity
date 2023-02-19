from solcx import compile_standard, install_solc
import json
with open("./simpleStorage.sol", "r") as file:
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
print(abi)
