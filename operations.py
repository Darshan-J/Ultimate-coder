from web3 import Web3 

def make_transaction():
    w3=Web3(Web3.IPCProvider("./datadirA/geth.ipc"))
    print("Connected: ",w3.isConnected())
    acc1_pubkey="0xb985f7A80B7678C1f6cdf4981Bf7ff2dF925C519"
    acc2_pubkey="0xB2AFd0e41Ac3AdF9B409669807B0A2BC39931280"
    with open("/home/kumarguru/Documents/Blockchain/ATTEMPT/datadirA/keystore/UTC--2020-01-08T06-32-30.894180037Z--b985f7a80b7678c1f6cdf4981bf7ff2df925c519") as keyfile:
        encrypted_key = keyfile.read()
        private_key = w3.eth.account.decrypt(encrypted_key, '**************')
        private_key=w3.toHex(private_key)
    transaction_details={
        "nonce":w3.eth.getTransactionCount(acc1_pubkey),
        "to":acc2_pubkey,
        "from":acc1_pubkey,
        "value":w3.toWei(5,"ether"),
        "gas": 2000000,
        "gasPrice": w3.toWei('50',"gwei")
    }
    signed_trans=w3.eth.account.signTransaction(transaction_details,private_key)
    tx_hash=w3.eth.sendRawTransaction(signed_trans.rawTransaction)
    #print(private_key)
    print(w3.toHex(tx_hash))

if __name__=="__main__":
    make_transaction()
