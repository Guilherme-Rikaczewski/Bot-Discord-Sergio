from src.schemas.discord import (
    DiscordInteraction,
    DiscordInteractionResponse,
    DiscordInteractionResponseData,
    InteractionCallbackType
)
from src.services.dices import DiceService


class CommandDispatcher:
    def __init__(self):
        self.handlers = {
            "roll": DiceService()
        }

    async def dispatch(self, interaction: DiscordInteraction):
        if not interaction.data:
            return self.invalid_command_response()

        command = interaction.data.name

        handler = self.handlers.get(command)
        if not handler:
            return self.invalid_command_response()
        return await handler.execute(interaction)

    def invalid_command_response(self):
        return DiscordInteractionResponse(
            type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
            data=DiscordInteractionResponseData(
                content="Comando invalido."
            )
        )
