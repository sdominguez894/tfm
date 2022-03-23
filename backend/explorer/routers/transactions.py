from fastapi import APIRouter, Depends, HTTPException
from explorer.providers.providerfactory import BlockchainProvider
from explorer.providers.provider import ProviderInterface
from explorer.models.blockchains import Blockchains


router = APIRouter()


@router.get("/")
async def get_transactions(blockchain_id: Blockchains, 
                           provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    return provider.get_transactions()


@router.get("/{transaction_id}")
async def transaction_by_id(blockchain_id: Blockchains, transaction_id: str,
                            provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    try:
        transaction_data = provider.get_transaction_by_id(transaction_id)
        return transaction_data
    except :
        errMessage = f"Transaction with id {transaction_id} was not found"
        raise HTTPException(status_code=404, detail=errMessage)