import os

def get_env_variable(var_name):
    """Get the environment variable or return exception"""
    try:
        env_value = os.environ[var_name]
        print( env_value )
        return env_value
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        #raise Exception(error_msg)


"""
Set your own config/credentials here
"""

#CoinMarketCap API configuration
COINMARKETCAP_API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
COINMARKETCAP_API_KEY = os.environ["COINMARKETCAP_API_KEY"]

#Algorand configuration
ALGOD_TOKEN        = os.environ["ALGOD_TOKEN"]
ALGOD_ADDRESS      = "https://mainnet-algorand.api.purestake.io/ps2" 
INDEXER_ADDRESS    = "https://mainnet-algorand.api.purestake.io/idx2"

#Bitcoin configuration


#Cardano configuration
BLOCKFROST_PROJECT_ID = "mainnetugnPOWiXzieqDhohU5S1UWUsyvaXHLCz"

#Ethereum configuration
INFURA_URL = os.environ["INFURA_URL"]

#Terra configuration
TERRA_CHAIN_ID = "columbus-5"
TERRA_URL = "https://lcd.terra.dev"
