import requests
import os
from dotenv import load_dotenv

load_dotenv()

APPLICATION_ID = os.getenv("DISCORD_APPLICATION_ID")
GUILD_ID = os.getenv("DISCORD_GUILD_ID")
BOT_TOKEN = os.getenv("DISCORD_TOKEN")

url = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/guilds/{GUILD_ID}/commands"

headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json",
}

# data = {
#     "name": "ping",
#     "description": "Responde Pong!"
# }

data = {
    "name": "roll",
    "description": "Faz uma rolagem de dados!"
}
response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
