import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from routers   import address, blockchains, blocks, transactions, search, summary
from explorer_setup import ExplorerSetup

#Configure providers and services
ExplorerSetup.setup()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blockchains.router, prefix="/blockchains", tags=["blockchains"])
app.include_router(address.router, prefix="/{blockchain_id}/address", tags=["address"])
app.include_router(blocks.router, prefix="/{blockchain_id}/blocks", tags=["blocks"])
app.include_router(summary.router, prefix="/{blockchain_id}/summary", tags=["summary"])
app.include_router(search.router, prefix="/{blockchain_id}/search", tags=["search"])
app.include_router(transactions.router, prefix="/{blockchain_id}/transactions", tags=["transactions"])



@app.get("/")
async def root():
    """
    Redirect to the blockchains endpoint which returns all the available blockchain ids
    """
    return RedirectResponse("/blockchains")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)