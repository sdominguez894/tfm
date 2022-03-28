from explorer.providers.provider import ProviderInterface
from explorer.providers.provider_factory import BlockchainProvider
from explorer.models.blockchains import Blockchains
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/{search_text}")
async def element_by_id(blockchain_id: Blockchains, search_text: str,
                        provider: ProviderInterface = Depends(BlockchainProvider.get_instance)):
    try:
        return provider.search_resource(search_text)
    except:
        errMessage = f"{search_text} was not found"
        raise HTTPException(status_code=404, detail=errMessage)
    return data