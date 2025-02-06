"""Clase que contiene el modulo para enviar textos bases previamente guardados."""

#External libraries
import random

from discord.ext import commands

#Ouwn libraries
import utils.text_loader as tl


class Copypaste(commands.Cog):
    """Clase que contiene el modulo para enviar textos bases previamente guardados."""

    def __init__(self, bot):
        """Inicializa el bot.
        args:
            bot (commands.Bot): Bot de discord.
            
    """
        self.bot = bot
        self.copypaste = tl.text_loader('copypaste.txt')


    @commands.command()
    async def copypaste(self, ctx):
        """Envía un texto base.
        args:
            ctx (commands.Context): Contexto de discord.
            query: Texto base a enviar.
            
        """
        num = random.randint(0, len(self.copypaste)-1)

        await ctx.send(self.copypaste[num])


async def setup(bot):
    """Añade el cog al bot.
    args:
        bot (commands.Bot): Bot de discord.
        
"""
    await bot.add_cog(Copypaste(bot))
    