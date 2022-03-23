from fastapi import APIRouter, HTTPException
from explorer.models.blockchains import Blockchains

router = APIRouter()


@router.get("/")
async def blockchains():
    return Blockchains.get_available_blockchains()


@router.get("/{blockchain_id}")
async def get_blockchain_details_by_id(blockchain_id: Blockchains):
    #TODO - Check if id exists
    data = { 
        "network" : blockchain_id,
        "summary" : {
            "marketCap" : "some_value", # API CoinmarketCap
            "price" : "some_value",
            "difficulty" : "some_value",
            "hashrate" : "some_value"
        },
    }
    return data