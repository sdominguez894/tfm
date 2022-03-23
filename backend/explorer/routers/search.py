from explorer.models.blockchains import Blockchains
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/{element_id}")
async def element_by_id(blockchain_id: Blockchains, element_id: str, ):
    #TODO - Detect element type
    #TODO - Fetch data or return exception
    data = { 
        "id" : "element_id",
        "element" : "element_data"
    }
    return data