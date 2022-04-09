from fastapi import APIRouter, Depends, HTTPException
from multichain_explorer.src.providers.provider_factory import BlockchainProvider
from multichain_explorer.src.providers.provider import ProviderInterface
from multichain_explorer.src.models.blockchains import Blockchains


router = APIRouter()


@router.get("/")
async def get_summary(blockchain_id: Blockchains,
                      provider: ProviderInterface = Depends(BlockchainProvider.get_instance) ):
    """
    Get the blockchain summary

    Args:
        blockchain_id: the blockchain id
        provider: the blockchain provider (injected)
        
    Returns:
        The blockchain summary as a dict
    
    Raises:
        HTTPException: if the blockchain id is not valid
    """
    try:
        return provider.get_summary()
    except Exception as e:
        errMessage = f"Summary information could not be obtained"
        raise HTTPException(status_code=404, detail=errMessage)