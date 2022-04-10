from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from multichain_explorer.src.models.blockchains import Blockchains

router = APIRouter()


@router.get("/")
async def blockchains():
    """
    Get all the blockchain id's
    
    Returns:
        The blockchains ids as a list
    """
    return Blockchains.get_available_blockchains()


@router.get("/{blockchain_id}")
async def get_blockchain_details_by_id(blockchain_id: Blockchains):
    """
    Get the blockchain summary by blockchain id

    Args:
        blockchain_id: the blockchain id
    
    Returns:
        The blockchain summary as a dict
    
    Raises:
        HTTPException: if the blockchain id is not valid
    """
    return RedirectResponse(f"/{blockchain_id.value}/summary")