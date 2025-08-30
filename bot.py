import os
import sys
import asyncio
import discord
from discord.ext import commands

# Banner box
banner = r"""
+-------------------+
|   Made by LOWCLAS |
+-------------------+
"""

def ask(prompt):
    print(prompt, end="", flush=True)
    return sys.stdin.readline().strip()

async def main():
    # Print the banner
    print(banner)

    token = ask("Enter your Discord Bot Token: ")
    if not token:
        print("No token provided. Exiting.")
        return

    channel_id = ask("Enter the Channel ID where the bot should reply: ")
    if not channel_id.isdigit():
        print("Invalid CHANNEL_ID. Must be numeric.")
        return
    os.environ["CHANNEL_ID"] = channel_id

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"✅ Logged in as {bot.user} | Responding only in channel {channel_id}")

    # Load your AI chat cog
    await bot.load_extension("cogs.ai_chat")
    await bot.start(token)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nShutting down…")
