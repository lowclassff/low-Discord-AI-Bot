import os
import asyncio
import discord
from discord.ext import commands

class AIClient:
    def __init__(self):
        self.provider = None
        self.client = None

        if os.getenv("OPENAI_API_KEY"):
            from openai import OpenAI
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.provider = "openai"
        elif os.getenv("GEMINI_API_KEY"):
            import google.generativeai as genai
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            self.client = genai.GenerativeModel("gemini-1.5-flash")
            self.provider = "gemini"
        elif os.getenv("OPENROUTER_API_KEY"):
            from openai import OpenAI
            self.client = OpenAI(
                api_key=os.getenv("OPENROUTER_API_KEY"),
                base_url="https://openrouter.ai/api/v1"
            )
            self.provider = "openrouter"
        else:
            raise RuntimeError(
                "No AI key found. Set one of: OPENAI_API_KEY, GEMINI_API_KEY, OPENROUTER_API_KEY"
            )

    async def chat(self, user_message: str) -> str:
        try:
            if self.provider in ("openai", "openrouter"):
                model = os.getenv("AI_MODEL", "gpt-4o-mini")
                resp = self.client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a helpful, friendly assistant."},
                        {"role": "user", "content": user_message}
                    ]
                )
                return resp.choices[0].message.content.strip()
            elif self.provider == "gemini":
                prompt = f"You are a helpful assistant. User: {user_message}"
                resp = self.client.generate_content(prompt)
                return (resp.text or "").strip()
        except Exception as e:
            return f"⚠️ AI error: {e}"

class AIChat(commands.Cog):
    def __init__(self, bot: commands.Bot, channel_id: int):
        self.bot = bot
        self.channel_id = channel_id
        self.ai = AIClient()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if message.channel.id != self.channel_id:
            return

        async with message.channel.typing():
            await asyncio.sleep(2)
            reply = await self.ai.chat(message.content)
            if reply and len(reply) > 1900:
                reply = reply[:1900] + "…"
            await message.channel.send(reply or "I couldn't generate a reply.")

async def setup(bot: commands.Bot):
    channel_id = os.getenv("CHANNEL_ID")
    if not channel_id:
        raise RuntimeError("Set CHANNEL_ID environment variable.")
    await bot.add_cog(AIChat(bot, int(channel_id)))