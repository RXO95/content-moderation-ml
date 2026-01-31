import os
import json
import requests
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
API_URL = os.getenv("API_URL")

WARNINGS_FILE = "discord_bot/warnings.json"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def load_warnings():
    if not os.path.exists(WARNINGS_FILE):
        return {}
    with open(WARNINGS_FILE, "r") as f:
        return json.load(f)


def save_warnings(data):
    with open(WARNINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)


@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    channel = message.channel
    user = message.author
    content = message.content

    payload = {"text": content}

    try:
        response = requests.post(API_URL, json=payload, timeout=5)

        # 🔒 SAFETY CHECK 1
        if response.status_code != 200:
            print("API returned status:", response.status_code)
            print("Response text:", response.text)
            return

        # 🔒 SAFETY CHECK 2
        try:
            result = response.json()
        except Exception:
            print("Invalid JSON from API:")
            print(response.text)
            return

        if result.get("toxic") is True:
            await message.delete()

            warnings = load_warnings()
            user_id = str(user.id)

            warnings[user_id] = warnings.get(user_id, 0) + 1
            save_warnings(warnings)

            count = warnings[user_id]

            if count < 3:
                await channel.send(
                    f"⚠️ {user.mention} Warning {count}/3 — Toxic content detected."
                )
            else:
                await channel.send(
                    f"⛔ {user.mention} reached 3 warnings and will be muted."
                )

                try:
                    await user.timeout(
                        duration=300,
                        reason="Repeated toxic messages"
                    )
                except Exception:
                    await channel.send(
                        "⚠️ Bot does not have permission to timeout users."
                    )

    except Exception as e:
        print("API connection error:", e)


client.run(TOKEN)
