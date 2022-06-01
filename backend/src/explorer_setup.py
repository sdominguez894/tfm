import config
from multichain_explorer.src.providers.ada.ada_provider import AdaProvider
from multichain_explorer.src.providers.algo.algo_provider import AlgoProvider
from multichain_explorer.src.providers.btc.btc_provider import BtcProvider
from multichain_explorer.src.providers.eth.eth_provider import EthProvider
from multichain_explorer.src.providers.luna.luna_provider import LunaProvider
from multichain_explorer.src.services.coinmarketcap_service import CoinMarketCapService


class ExplorerSetup:

    @staticmethod
    def setup():

        #CoinMarketCap configuration
        CoinMarketCapService.COINMARKETCAP_API_URL = config.COINMARKETCAP_API_URL
        CoinMarketCapService.COINMARKETCAP_API_KEY = config.COINMARKETCAP_API_KEY

        #Bitcoin configuration
        

        #Algorand configuration
        AlgoProvider.ALGOD_TOKEN     = config.ALGOD_TOKEN
        AlgoProvider.ALGOD_ADDRESS   = config.ALGOD_ADDRESS   
        AlgoProvider.INDEXER_ADDRESS = config.INDEXER_ADDRESS 

        #Cardano configuration
        AdaProvider.BLOCKFROST_PROJECT_ID = config.BLOCKFROST_PROJECT_ID

        #Ethereum configuration
        EthProvider.INFURA_URL = config.INFURA_URL    

        #Terra configuration
        LunaProvider.TERRA_CHAIN_ID = config.TERRA_CHAIN_ID
        LunaProvider.TERRA_URL      = config.TERRA_URL
