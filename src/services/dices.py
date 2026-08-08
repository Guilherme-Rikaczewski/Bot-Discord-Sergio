# type: ignore
from src.schemas.discord import (
    DiscordInteraction,
)
from src.services.base_service import BaseService
from src.utils.response_builder import ResponseBuilder
from random import randint


class DiceService(BaseService):
    async def execute(self, interaction: DiscordInteraction):
        if not interaction.data.options:
            return ResponseBuilder.message("Comando invalido.")

        expression = interaction.data.options[0].value
        try:
            result = self._roll(
                self._get_dice_expression_info(
                    expression
                )
            )
        except ValueError as error:
            return ResponseBuilder.message(error.args[0])

        return ResponseBuilder.message(f"Rolando {expression}: {result}")

    @staticmethod
    def _get_dice_expression_info(expression: str) -> dict:
        add = 0
        sub = 0
        number, sides = expression.lower().split("d")

        if number == '':
            number = 1

        if "+" in sides and "-" in sides:
            raise ValueError(
                f'''Informe apenas uma expressão matemática por vez.
"{expression}" possui mais de uma.'''
            )
        elif "+" in sides:
            sides, add = sides.split('+')
        elif "-" in sides:
            sides, sub = sides.split('-')

        return {
            "number": int(number),
            "sides": int(sides),
            "add": int(add),
            "sub": int(sub)
        }

    @staticmethod
    def _roll(expression_info: dict) -> int:
        result = 0
        for _ in range(expression_info["number"]):
            result += randint(1, expression_info["sides"])

        return result+expression_info["add"]-expression_info["sub"]
