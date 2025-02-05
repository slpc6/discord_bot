"""Punto de ejecucion del bot de discord."""

#External libraries
import discord
import os

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


async def load_cogs():
    """Cargar los cogs del bot.

"""
    await bot.load_extension("cogs.general")
    await bot.load_extension("cogs.music")

@bot.event
async def on_ready():
    """Muestra por consola cuando el bot esta listo para usarse.    
    
"""
    print(f'Bot conectado como {bot.user}')
    await load_cogs()

bot.run(TOKEN)
