import config
from multichain_explorer.src.providers.eth.eth_provider import EthProvider
from multichain_explorer.src.services.coinmarketcap_service import CoinMarketCapService


class ExplorerSetup:

    @staticmethod
    def setup():
        EthProvider.INFURA_URL = config.INFURA_URL
        CoinMarketCapService.API_KEY = config.COINMARKETCAP_API_KEY


