from src.schemas.discord import (
    DiscordInteraction,
)
from src.services.base_service import BaseService
from src.utils.response_builder import ResponseBuilder
from random import randint


class DiceService(BaseService):
    async def execute(self, interaction: DiscordInteraction):
        print("teste")
        return ResponseBuilder.message(f"Rolando 1d20: {randint(1, 20)}")
