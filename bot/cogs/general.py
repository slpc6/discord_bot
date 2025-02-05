"""Clase para los comando generales de un bot de discord."""

#External libraries
from discord.ext import commands

class General(commands.Cog):
    """Clase para los comando generales de un bot de discord."""

    def __init__(self, bot):
        """Inicializa el bot.
        args:
            bot (commands.Bot): Bot de discord.

"""
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
        """Comando para comprobar si el bot esta activo.
        args:
            ctx (commands.Context): Contexto del comando.

"""
        await ctx.send("¡Pong!")

async def setup(bot):
    """Añade el cog al bot.
    args:
        bot (commands.Bot): Bot de discord.
        
"""
    await bot.add_cog(General(bot))
