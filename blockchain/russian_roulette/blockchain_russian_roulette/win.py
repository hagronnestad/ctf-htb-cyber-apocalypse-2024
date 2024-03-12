from web3 import Web3

# Setup connection to Ethereum node
provider_url = 'http://94.237.49.182:54163'  # Update if necessary
w3 = Web3(Web3.HTTPProvider(provider_url))

# Check if connected to the provider
if not w3.is_connected():
    print("Failed to connect to the Ethereum node.")
else:
    chain_id = w3.eth.chain_id
    print(f"Successfully connected to the Ethereum node. Chain ID: {chain_id}")

# Define contract ABI and address
contract_abi = [
  {
    "inputs": [],
    "name": "pullTrigger",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]

contract_address = Web3.to_checksum_address('0xf9de1941EDAC16D09Bf46Ecfe2b8837d05AC7248')

# Create contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Account information
private_key = '0x37dc35f95b227104fdf157ae76c6b62fd39afa65bfe6acfa95a6acff3343c692'
account_address = Web3.to_checksum_address('0x98f1AF4b0334fB32CF226910ece24d6BdB41aC8b')  # Derived from the private key

account_balance = w3.eth.get_balance(account_address)
print(f"Account balance: {w3.from_wei(account_balance, 'ether')} ETH")

# Ensure your account is unlocked and has Ether for gas if required

# Prepare transaction
nonce = w3.eth.get_transaction_count(account_address)
transaction = contract.functions.pullTrigger().build_transaction({
    'chainId': 31337,  # Update with the correct chain ID
    'gas': 2000000,
    'gasPrice': w3.to_wei('50', 'gwei'),
    'nonce': nonce,
})

# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for the transaction to be mined
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction receipt: {tx_receipt}")
