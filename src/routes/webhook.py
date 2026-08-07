from fastapi import APIRouter, Request, HTTPException
from src.schemas.discord import (
    DiscordInteraction,
    DiscordInteractionResponse,
    InteractionType,
)
from src.services.dispatcher import CommandDispatcher
from src.utils.response_builder import ResponseBuilder
from src.utils.validator import verify_discord_signature

router = APIRouter(prefix="/webhook", tags=["Webhook"])
dispatcher = CommandDispatcher()


@router.post('/', response_model=DiscordInteractionResponse)
async def webhook(request: Request):
    body = await request.body()

    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]

    if not signature or not timestamp:
        raise HTTPException(401)

    if not verify_discord_signature(signature, timestamp, body):
        raise HTTPException(401)

    interaction = DiscordInteraction.model_validate_json(body)

    if interaction.type == InteractionType.PING:
        return ResponseBuilder.pong()

    return await dispatcher.dispatch(interaction)
