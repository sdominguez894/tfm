from multichain_explorer.src.models.provider_options import ProviderOptions
from fastapi import APIRouter, Depends, HTTPException
from multichain_explorer.src.providers.provider_factory import BlockchainProvider
from multichain_explorer.src.providers.provider import ProviderInterface
from multichain_explorer.src.models.blockchains import Blockchains


router = APIRouter()


@router.get("/")
async def blocks(blockchain_id: Blockchains, raw: str = 'False',
                 provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    """
    Get a list of blocks of a blockchain

    Args:
        blockchain_id: the blockchain id
        raw: whether to return the raw block data or not (query parameter, default: False)
        provider: the blockchain provider (injected)
    
    Returns:
        The blocks as a list
    """
    num_blocks = 10
    rawOpt = raw == 'True'
    options = ProviderOptions(rawOpt)
    return provider.get_blocks(10, options)


@router.get("/{block_id}")
async def get_block_by_id(block_id: str, raw: str = 'False',
                          provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    """"
    Get block by its id

    Args:
        block_id: the block id
        raw: whether to return the raw block data or not (query parameter, default: False)
        provider: the blockchain provider (injected)

    Returns:
        The block as a dict

    Raises:
        HTTPException: if the block id is not valid
    """
    rawOpt = raw == 'True'
    options = ProviderOptions(rawOpt)
    try:
        return provider.get_block_by_id(block_id, options)
    except :
        errMessage = f"Block number {block_id} was not found"
        raise HTTPException(status_code=404, detail=errMessage)
