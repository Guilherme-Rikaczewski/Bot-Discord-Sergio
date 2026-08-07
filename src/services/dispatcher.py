from src.schemas.discord import (
    DiscordInteraction,
)
from src.services.dices import DiceService
from src.utils.response_builder import ResponseBuilder


class CommandDispatcher:
    def __init__(self):
        self.handlers = {
            "roll": DiceService()
        }

    async def dispatch(self, interaction: DiscordInteraction):
        if not interaction.data:
            return ResponseBuilder.message("Comando invalido.")

        command = interaction.data.name

        handler = self.handlers.get(command)
        if not handler:
            return ResponseBuilder.message("Comando invalido.")
        return await handler.execute(interaction)
