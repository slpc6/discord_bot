

import discord
import io
import os
import requests

from discord.ext import commands
from PIL import Image


class ImageGeneration(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.getenv("DEEPAI_API_KEY")

    @commands.command()
    async def generate(self, ctx, *, prompt: str):
        """Genera una imagen a partir de un texto usando DeepAI."""
        await ctx.send(f"🖌️ Generando imagen para: **{prompt}**...")

        try:
            # Hacer una solicitud a la API de DeepAI
            response = requests.post(
                "https://api.deepai.org/api/text2img",
                data={"text": prompt},
                headers={"api-key": self.api_key}
            )
            response.raise_for_status()

            # Obtener la URL de la imagen generada
            image_url = response.json()["output_url"]

            # Descargar la imagen
            image_response = requests.get(image_url)
            image_response.raise_for_status()

            # Convertir la imagen a un archivo de Discord
            image = Image.open(io.BytesIO(image_response.content))
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            buffer.seek(0)

            # Enviar la imagen al canal de Discord
            await ctx.send(file=discord.File(buffer, filename="generated_image.png"))
        
        except Exception as e:
            await ctx.send(f"❌ Ocurrió un error al generar la imagen: {e}")
    

async def setup(bot):
    await bot.add_cog(ImageGeneration(bot))