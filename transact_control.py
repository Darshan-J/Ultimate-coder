from web3 import Web3
gurl="HTTP://127.0.0.1:7545"
w3=Web3(Web3.HTTPProvider(gurl))
print(w3.isConnected())
acc1="0x6195DeD3bd6E9386e38EB3B98adD2655215b301A"
acc2="0x468082718f6d82E72581e4de041aAD1597877cf7"
ac1_priv_key="1e28716ba3723fde5875324f2705f04c34756296742ac774b8e159251eacf274"

trans_1={
    "nonce":w3.eth.getTransactionCount(acc1),
    "to":acc2,
    "from":acc1,
    "value":w3.toWei(25,"ether"),
    "gas": 2000000,
    "gasPrice": w3.toWei('50',"gwei")
}

signed_trans=w3.eth.account.signTransaction(trans_1,ac1_priv_key)
tx_hash=w3.eth.sendRawTransaction(signed_trans.rawTransaction)
print(w3.toHex(tx_hash))

