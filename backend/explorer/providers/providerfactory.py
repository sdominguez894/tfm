
from explorer.providers.eth.eth_provider import EthProvider
from explorer.providers.provider import ProviderInterface
from explorer.models.blockchains import Blockchains

class BlockchainProvider():

    def get_instance(blockchain_id: Blockchains) -> ProviderInterface:
        match blockchain_id:
            case Blockchains.BTC:
                return None
            case Blockchains.ETH:
                return EthProvider()
            case Blockchains.ADA:
                return None
            case Blockchains.ALGO:
                return None
            case Blockchains.LUNA:
                return None