from multichain_explorer.src.models.provider_options import ProviderOptions
from fastapi import APIRouter, Depends, HTTPException
from multichain_explorer.src.providers.provider_factory import BlockchainProvider
from multichain_explorer.src.providers.provider import ProviderInterface
from multichain_explorer.src.models.blockchains import Blockchains


router = APIRouter()


@router.get("/")
async def get_transactions(blockchain_id: Blockchains, raw: str = 'False',
                           provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    
    num_transactions = 10
    rawOpt = raw == 'True'
    options = ProviderOptions(rawOpt)
    
    return provider.get_transactions(num_transactions, options)


@router.get("/{transaction_id}")
async def get_transaction_by_id(blockchain_id: Blockchains, transaction_id: str, raw: str = 'False',
                                provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    """Returns a transaction by its id

    Args:
        blockchain_id: the blockchain id
        transaction_id: the transaction id
        raw: whether to return the raw transaction data or not
        provider: the blockchain provider
   
    Returns:
        The transaction as a dict

    Raises:
        HTTPException: if the transaction id is not valid
    """
    rawOpt = raw == 'True'
    options = ProviderOptions(rawOpt)
    
    try:
        transaction_data = provider.get_transaction_by_id(transaction_id, options)
        return transaction_data
    except :
        errMessage = f"Transaction with id {transaction_id} was not found"
        raise HTTPException(status_code=404, detail=errMessage)