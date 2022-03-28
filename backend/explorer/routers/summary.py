from fastapi import APIRouter, Depends, HTTPException
from explorer.providers.provider_factory import BlockchainProvider
from explorer.providers.provider import ProviderInterface
from explorer.models.blockchains import Blockchains


router = APIRouter()


@router.get("/")
async def get_summary(blockchain_id: Blockchains,
                      provider: ProviderInterface = Depends(BlockchainProvider.get_instance) ):
    try:
        print("calling summary")
        return provider.get_summary()
    except Exception as e:
        print(e)
        errMessage = f"Summary information could not be obtained"
        raise HTTPException(status_code=404, detail=errMessage)