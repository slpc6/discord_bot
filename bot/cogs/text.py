"""Clase que contiene el modulo para enviar textos bases previamente guardados."""

import random
from discord.ext import commands


from database.mongo import MongoDBClientSingleton


class Copypaste(commands.Cog):
    """Clase que contiene el modulo para enviar textos bases previamente guardados."""


    def __init__(self, bot):
        self.bot = bot
        mongo_client = MongoDBClientSingleton()
        db = mongo_client.get_collection('DISCORD_BOT', 'copypaste').database
        self.copypaste_collection = db['copypaste']
        self.david_collection = db['david']


    @commands.command()
    async def copypaste(self, ctx):
        """Envía un texto base aleatorio desde la base de datos."""
        count = self.copypaste_collection.count_documents({})
        if count == 0:
            await ctx.send("No hay textos disponibles en la base de datos.")
            return
        random_index = random.randint(0, count - 1)
        doc = self.copypaste_collection.find().skip(random_index).limit(1)[0]
        await ctx.send(doc['texto'])


    @commands.command()
    async def david(self, ctx):
        """Insulta a david con un texto aleatorio desde la base de datos."""
        count = self.david_collection.count_documents({})
        if count == 0:
            await ctx.send("No hay insultos disponibles en la base de datos.")
            return
        random_index = random.randint(0, count - 1)
        doc = self.david_collection.find().skip(random_index).limit(1)[0]
        await ctx.send(doc['texto'])


async def setup(bot):
    await bot.add_cog(Copypaste(bot))
    