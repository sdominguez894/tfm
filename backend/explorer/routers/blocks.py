from explorer.models.provider_options import ProviderOptions
from fastapi import APIRouter, Depends, HTTPException
from explorer.providers.provider_factory import BlockchainProvider
from explorer.providers.provider import ProviderInterface
from explorer.models.blockchains import Blockchains


router = APIRouter()


@router.get("/")
async def blocks(blockchain_id: Blockchains, raw: str = 'False',
                 provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):

    num_blocks = 10
    rawOpt = raw == 'True'
    options = ProviderOptions(rawOpt)
    return provider.get_blocks(10, options)


@router.get("/{block_id}")
async def get_block_by_id(block_id: str, raw: str = 'False',
                          provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    rawOpt = raw == 'True'
    options = ProviderOptions(rawOpt)
    try:
        return provider.get_block_by_id(block_id, options)
    except :
        errMessage = f"Block number {block_id} was not found"
        raise HTTPException(status_code=404, detail=errMessage)
