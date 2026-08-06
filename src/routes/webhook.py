from fastapi import APIRouter, HTTPException


router = APIRouter(prefix="webhook", tags=["Webhook"])


@router.post('/')
async def webhook():
    try:
        return
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(500, detail=f'Internal server error {error}')
