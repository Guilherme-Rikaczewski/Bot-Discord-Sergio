from fastapi import APIRouter, HTTPException
from src.schemas.discord import (
    DiscordInteraction,
    DiscordInteractionResponse,
    DiscordInteractionResponseData,
    InteractionType,
    InteractionCallbackType
)
from src.services.dispatcher import CommandDispatcher


router = APIRouter(prefix="webhook", tags=["Webhook"])
dispatcher = CommandDispatcher()


@router.post('/', response_model=DiscordInteractionResponse)
async def webhook(interaction: DiscordInteraction):
    if interaction.type == InteractionType.PING:
        return DiscordInteractionResponse(
            type=InteractionCallbackType.PONG,
            data=DiscordInteractionResponseData(
                content="PINGOU."
            )
        )

    return await dispatcher.dispatch(interaction)
