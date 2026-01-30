import os
import requests
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
API_URL = os.getenv("API_URL")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    payload = {"text": message.content}

    try:
        response = requests.post(API_URL, json=payload, timeout=3)
        result = response.json()

        if result.get("toxic"):
            await message.delete()
            await message.channel.send(
                f"⚠️ {message.author.mention}, your message was removed due to toxic content."
            )

    except Exception as e:
        print("API error:", e)


client.run(TOKEN)
