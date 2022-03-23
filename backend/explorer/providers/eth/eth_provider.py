from .      import config
from web3   import Web3
from explorer.providers.provider import ProviderInterface


class EthProvider(ProviderInterface):
    
    def __init__(self):
        self.provider = Web3(Web3.HTTPProvider(config.INFURA_URL))


    def get_summary(self):
        return { "TODO": "SUMMARY" }


    def get_blocks(self, num_blocks = 10):
        fake_data = {
            "name"          : "ETH",
            "price"         : "some_value",
            "marketCap"     : "some_value",
            "difficulty"    : "some_value",
            "hashrate"      : "some_value"
        }
        return fake_data

    def get_blocks(self, num_blocks = 10):
        latest_blocks = []
        # Multiple synchronous call, would be nice if they were asynchronous
        for block_number in range(self.provider.eth.block_number, 
                                  self.provider.eth.block_number-num_blocks, 
                                  -1):
            block_data = self.get_block_by_id(block_number)
            latest_blocks.append(block_data)
        return latest_blocks


    def get_block_by_id(self, block_id = 'latest'):
        #If id is a number cast to int
        if type(block_id) == str and block_id.isnumeric():
            block_id = int(block_id)
        
        try:
            block = self.provider.eth.get_block(block_id)
            block_data = {
                "id" : block.number,
                "miner" : block.miner,
                "difficulty" : block.difficulty,
                "timestamp": block.timestamp
            }
        except ValueError as err:
            # Log exception
            raise

        return block_data


    def get_transactions(self, num_tx = 10):
        try:
            block = self.provider.eth.get_block("latest")
            block_transactions = block.transactions
            latest_transactions = []

            # Get the last num_tx transactions from block (default is 10)
            for transaction_id in block_transactions[-num_tx:]:
                #Convert id from binary hex to string
                transaction_data = self.get_transaction_by_id(transaction_id.hex())
                latest_transactions.append(transaction_data)

        except ValueError as err:
            # Log exception
            raise
        return latest_transactions


    def get_transaction_by_id(self, tx_id = 'latest'):
        transaction = self.provider.eth.get_transaction(tx_id)
        transaction_data = {
            "id"    : tx_id,
            "from"  : transaction['from'],
            "to"    : transaction['to'],
            "value" : transaction['value'],
            "block" : transaction['blockNumber']
        }
        return transaction_data


    def get_address_details_by_id(self, address_id):
        try:
            balance = self.provider.eth.get_balance(address_id)
            balance = self.provider.fromWei(balance, 'ether')
            return {
                "address"   : address_id,
                "balance"   : balance
            }
        except Exception as err:
            #log error
            raise
