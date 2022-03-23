from fastapi import APIRouter, Depends, HTTPException
from explorer.providers.providerfactory import BlockchainProvider
from explorer.providers.provider import ProviderInterface
from explorer.models.blockchains import Blockchains


router = APIRouter()


@router.get("/{address_id}")
async def get_addres_by_id(blockchain_id: Blockchains, address_id: str,
                           provider: ProviderInterface = Depends(BlockchainProvider.get_instance) ):
    try:
        return provider.get_address_details_by_id(address_id)
    except:
        errMessage = f"Address {address_id} was not found"
        raise HTTPException(status_code=404, detail=errMessage)