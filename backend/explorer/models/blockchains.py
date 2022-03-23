from enum import Enum

class Blockchains(Enum):
    ETH = "ETH"
    BTC = "BTC"
    ADA = "ADA"
    ALGO = "ALGO"
    LUNA = "LUNA"

    def get_available_blockchains():
        available_blockchains = [] 
        for blockchain in Blockchains:
            available_blockchains.append(blockchain)
        return available_blockchains