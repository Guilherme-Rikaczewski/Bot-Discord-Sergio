from fastapi import APIRouter
from src.schemas.discord import (
    DiscordInteraction,
    DiscordInteractionResponse,
    InteractionType,
)
from src.services.dispatcher import CommandDispatcher
from src.utils.response_builder import ResponseBuilder


router = APIRouter(prefix="webhook", tags=["Webhook"])
dispatcher = CommandDispatcher()


@router.post('/', response_model=DiscordInteractionResponse)
async def webhook(interaction: DiscordInteraction):
    if interaction.type == InteractionType.PING:
        return ResponseBuilder.pong()

    return await dispatcher.dispatch(interaction)
