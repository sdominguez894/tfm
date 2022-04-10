from fastapi import APIRouter, Depends, HTTPException
from multichain_explorer.src.providers.provider_factory import BlockchainProvider
from multichain_explorer.src.providers.provider import ProviderInterface
from multichain_explorer.src.models.blockchains import Blockchains


router = APIRouter()


@router.get("/{address_id}")
async def get_addres_by_id(blockchain_id: Blockchains, address_id: str,
                           provider: ProviderInterface = Depends(BlockchainProvider.get_instance) ):
    """
    Get a blockchain address by its id

    Args:
        blockchain_id: the blockchain id
        address_id: the address id
        provider: the blockchain provider

    Returns:
        The address as a dict

    Raises:
        HTTPException: if the address id is not valid
    """
    try:
        return provider.get_address(address_id)
    except:
        errMessage = f"Address {address_id} was not found"
        raise HTTPException(status_code=404, detail=errMessage)