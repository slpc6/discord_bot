import discord
import os
import yt_dlp

from discord.ext import commands
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Configurar intents y prefijo
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')


@bot.command()
async def ping(ctx):
    await ctx.send("¡Pong!")


@bot.command()
async def join(ctx):
    """El bot se une al canal de voz del usuario."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("Me uní al canal de voz ✅")
    else:
        await ctx.send("¡Debes estar en un canal de voz!")


@bot.command()
async def leave(ctx):
    """El bot sale del canal de voz."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Salí del canal de voz ✅")
    else:
        await ctx.send("No estoy en un canal de voz.")


@bot.command()
async def play(ctx, url: str):
    """Reproduce audio en streaming desde YouTube."""
    if not ctx.voice_client:
        await ctx.invoke(join)  # Unirse al canal si no está conectado

    await ctx.send("🎵 Obteniendo enlace de audio...")

    # Obtener URL de transmisión directa desde YouTube
    ydl_opts = {'format': 'bestaudio', 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']  # URL del audio en streaming

    await ctx.send("🎶 Reproduciendo...")

    # Reproducir el audio en streaming
    ctx.voice_client.stop()
    audio_source = discord.FFmpegPCMAudio(audio_url, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
    ctx.voice_client.play(audio_source)


bot.run(TOKEN)
