

from openai import OpenAI

from discord.ext import commands
from PIL import Image

import config

class ImageGeneration(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.api_key = config.API_KEY

    @commands.command()
    async def generate(self, ctx, *, prompt: str):
        """Genera una imagen a partir de un texto usando DeepAI."""
        await ctx.send(f"🖌️ Generando imagen para: **{prompt}**...")

        try:
            client = OpenAI(api_key = config.API_KEY)

            response = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": prompt,
                }],
                model="dall-e-3",
            )

            await ctx.send(response)
        except Exception as e:
            await ctx.send(f"❌ Error al obtener respuesta: {e}")
    

async def setup(bot):
    await bot.add_cog(ImageGeneration(bot))