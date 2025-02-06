"""Clase que permite conectar un bot de discord con la api de open ia"""

#External libraries
from discord.ext import commands
from openai import OpenAI

#Own Libraries
from config import config


class Gpt(commands.Cog):
    """Clase que permite conectar un bot de discord con la api de open ia"""


    def __init__(self, bot):
        self.bot = bot
        self.api_key =  config.API_KEY


    @commands.command()
    async def gpt(self, ctx, *, query: str):
        """Responde a una consulta utilizando la API de DeepSeek."""

        await ctx.send(f"🔍 Buscando respuesta para: **{query}**...")

        if not query:
            await ctx.send(f"❌ Debes escribir una pregunta después de `$gpt`.")
        
        try:

            client = OpenAI(api_key = config.API_KEY)

            response = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": "Say this is a test",
                }],
                model="gpt-4o-mini-2024-07-18",
            )
            await ctx.send(response)
        except Exception as e:
            await ctx.send(f"❌ Error al obtener respuesta: {e}")


async def setup(bot):
    await bot.add_cog(Gpt(bot))
