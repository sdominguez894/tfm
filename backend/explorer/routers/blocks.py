from fastapi import APIRouter, Depends, HTTPException
from explorer.providers.providerfactory import BlockchainProvider
from explorer.providers.provider import ProviderInterface
from explorer.models.blockchains import Blockchains


router = APIRouter()


@router.get("/")
async def blocks(blockchain_id: Blockchains, 
                 provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    return provider.get_blocks()


@router.get("/{block_id}")
async def transaction_by_id(block_id: str,
                            provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    try:
        return provider.get_block_by_id(block_id)
    except :
        errMessage = f"Block number {block_id} was not found"
        raise HTTPException(status_code=404, detail=errMessage)
