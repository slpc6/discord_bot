"""Clase para el manejo de imágenes y videos en el bot de discord."""

#External libraries
from discord.ext import commands
import discord
from database.mongo import MongoDBClientSingleton
import random
from io import BytesIO


class Picture(commands.Cog):
    """Cog para enviar imágenes y videos almacenados en MongoDB Atlas."""


    def __init__(self, bot):
        self.bot = bot
        mongo_client = MongoDBClientSingleton()
        db = mongo_client.get_collection('DISCORD_BOT', 'foto').database
        self.foto_collection = db['foto']
        self.video_collection = db['video']


    @commands.command()
    async def image(self, ctx):
        """Envía una imagen aleatoria desde la base de datos."""
        try:
            count = self.foto_collection.count_documents({})
            if count == 0:
                await ctx.send("No hay imágenes disponibles en la base de datos.")
                return
            random_index = random.randint(0, count - 1)
            doc = self.foto_collection.find().skip(random_index).limit(1)[0]
            file_bytes = doc['data']
            filename = doc.get('filename', 'imagen.jpg')
            # Usar BytesIO para asegurar que se maneje como binario
            await ctx.send(file=discord.File(fp=BytesIO(file_bytes), filename=filename))
        except Exception as e:
            await ctx.send(f"Error al enviar la imagen: {str(e)}")


    @commands.command()
    async def video(self, ctx):
        """Envía un video aleatorio desde la base de datos."""
        try:
            count = self.video_collection.count_documents({})
            if count == 0:
                await ctx.send("No hay videos disponibles en la base de datos.")
                return
            random_index = random.randint(0, count - 1)
            doc = self.video_collection.find().skip(random_index).limit(1)[0]
            file_bytes = doc['data']
            filename = doc.get('filename', 'video.mp4')
            # Usar BytesIO para asegurar que se maneje como binario
            await ctx.send(file=discord.File(fp=BytesIO(file_bytes), filename=filename))
        except Exception as e:
            await ctx.send(f"Error al enviar el video: {str(e)}")


async def setup(bot):
    await bot.add_cog(Picture(bot))