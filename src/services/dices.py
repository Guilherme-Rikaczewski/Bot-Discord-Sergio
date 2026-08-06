from src.schemas.discord import (
    DiscordInteraction,
)
from src.services.base_service import BaseService


class DiceService(BaseService):
    async def execute(self, interaction: DiscordInteraction):
        pass
