from explorer.models.provider_options import ProviderOptions
from fastapi import APIRouter, Depends, HTTPException
from explorer.providers.provider_factory import BlockchainProvider
from explorer.providers.provider import ProviderInterface
from explorer.models.blockchains import Blockchains


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

    rawOpt = raw == 'True'
    options = ProviderOptions(rawOpt)
    
    try:
        transaction_data = provider.get_transaction_by_id(transaction_id, options)
        return transaction_data
    except :
        errMessage = f"Transaction with id {transaction_id} was not found"
        raise HTTPException(status_code=404, detail=errMessage)