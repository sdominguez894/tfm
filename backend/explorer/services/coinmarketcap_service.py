from .      import config
from explorer.services.fetch_service import FetchService

class CoinMarketCapService():
    
    currency : str
    fetchService : FetchService

    def __init__(self):
        self.currency = "USD"
        self.fetchService : FetchService()

    def fetchData(self, symbol: str):
        try:
            params = self.get_params(symbol)
            headers = self.get_headers()

            #TODO - Use class member service
            data = FetchService().fetchJson(
                                        config.COINMARKETCAP_URL,
                                        params,
                                        headers
                                    )
            return data
        except Exception as e:
            print(e)
            raise


    def get_params(self, symbol: str):
        parameters = {
            'symbol': symbol,
            'convert': self.currency
        }
        return parameters

    def get_headers(self):
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': config.COINMARKETCAP_API_KEY
        }
        return headers

