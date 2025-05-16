"""Punto de ejecucion del bot de discord."""

#External libraries
import discord
import os
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import config
from path import path
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)
app = FastAPI(version="1.0.0", title="Discord bot", description="")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

if __name__ == "__main__":
    """Punto de inicio de la aplicacion, corre el servidor."""
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)

bot.run(config.TOKEN)
