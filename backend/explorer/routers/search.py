from multichain_explorer.src.providers.provider import ProviderInterface
from multichain_explorer.src.providers.provider_factory import BlockchainProvider
from multichain_explorer.src.models.blockchains import Blockchains
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/{search_text}")
async def element_by_id(blockchain_id: Blockchains, search_text: str,
                        provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    """
    Get a blockchain element by its id

    Args:
        blockchain_id: the blockchain id
        search_text: the element id
        provider: the blockchain provider

    Returns:
        The element as a dict

    Raises:
        HTTPException: if the element id is not valid
    """
    try:
        return provider.search_resource(search_text)
    except:
        errMessage = f"{search_text} was not found"
        raise HTTPException(status_code=404, detail=errMessage)