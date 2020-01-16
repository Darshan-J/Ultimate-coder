from web3 import Web3
import json
gurl="HTTP://127.0.0.1:7545"
w3=Web3(Web3.HTTPProvider(gurl))
w3.eth.defaultAccount=w3.eth.accounts[0]
address=w3.toChecksumAddress("0x4e0a2aA4a7148fDDAD18F71A90681359ed711B8e")
abi=json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
contract=w3.eth.contract(address=address,abi=abi)
#print(contract.functions.greet().call())
tx_hash=contract.functions.setGreeting("HELLOOOOOOOOOOOOOOOOOOO!").transact()
print(w3.toHex(tx_hash))
w3.eth.waitForTransactionReceipt(tx_hash)
print("Updated Greeting:{}".format(contract.functions.greet().call()))