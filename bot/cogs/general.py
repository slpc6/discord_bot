"""Clase para los comando generales de un bot de discord."""

#External libraries
from discord.ext import commands
import random

#Ouwn libraries
import utils.text_loader as tl


class General(commands.Cog):
    """Clase para los comando generales de un bot de discord."""


    def __init__(self, bot):
        """Inicializa el bot.
        args:
            bot (commands.Bot): Bot de discord.

    """
        self.bot = bot
        self.insultos = tl.text_loader('david.txt')

    @commands.command()
    async def ping(self, ctx):
        """Comando para comprobar si el bot esta activo.
        args:
            ctx (commands.Context): Contexto del comando.

    """
        await ctx.send("¡Pong!")

    
    @commands.command()
    async def david(self, ctx):
        """Insulta a david
        args:
            ctx: (commands.Context): Contexto del comando.
        
        """
        num = random.randint(0, len(self.insultos)-1)

        await ctx.send(self.insultos[num])
    

    @commands.command()
    async def info(self, ctx):
        """Responde con el link donde se ve la descripcion y funcionamiento del proyecto.
        args:
            ctx: (commands.Context): Contexto del comando.
        
        """
        await ctx.send('pagina de info del bot: https://discord-bot-x0nf.onrender.com/')


async def setup(bot):
    """Añade el cog al bot.
    args:
        bot (commands.Bot): Bot de discord.
        
    """
    await bot.add_cog(General(bot))
