"""Punto de ejecucion del bot de discord."""

#External libraries
import discord
import os


from config import config
from path import path
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)


async def load_cogs():
    """Cargar los cogs del bot.

    """
    cogs_path = path.cogs_path
    files = [f[:-3] for f in os.listdir(cogs_path) if f.endswith(".py") and f != "__init__.py"]
    
    for file in files:
        await bot.load_extension(f'cogs.{file}')


@bot.event
async def on_ready():
    """Muestra por consola cuando el bot esta listo para usarse.    
    
"""
    print(f'Bot conectado como {bot.user}')
    await load_cogs()


bot.run(config.TOKEN)
