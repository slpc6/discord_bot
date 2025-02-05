"""Clase que contiene el modulo de música para el bot de Discord."""

#External libraries
import discord
import yt_dlp

from discord.ext import commands

#Ouwn libraries
from utils.audio_queue import AudioQueue


class Music(commands.Cog):
    """Clase que contiene el modulo de música para el bot de Discord."""

    def __init__(self, bot):
        """Inicializa el bot.
        args:
            bot (commands.Bot): Bot de discord.
            
    """
        self.bot = bot
        self.queue = AudioQueue()


    @commands.command()
    async def join(self, ctx):
        """El bot se une al canal de voz del usuario.
        args:
            ctx (commands.Context): Contexto de discord.
            
        """
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send("Me uní al canal de voz ✅")
        else:
            await ctx.send("¡Debes estar en un canal de voz!")


    @commands.command()
    async def leave(self, ctx):
        """El bot sale del canal de voz.
        args:
            ctx (commands.Context): Contexto de discord.
            
        """
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Salí del canal de voz ✅")
        else:
            await ctx.send("No estoy en un canal de voz.")


    @commands.command()
    async def play(self, ctx, url: str):
        """Agrega una canción a la cola y reproduce.
        args:
            ctx (commands.Context): Contexto de discord.
            url (str): URL de la canción.
            
        """
        if not ctx.voice_client:
            await ctx.invoke(self.join)
        
        await ctx.send("🎵 Obteniendo enlace de audio...")

        ydl_opts = {'format': 'bestaudio', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']

        self.queue.add(audio_url)
        await ctx.send(f"🎶 {info['title']} ha sido añadida a la cola.")

        if not ctx.voice_client.is_playing():
            await self.play_next(ctx)


    async def play_next(self, ctx):
        """Reproduce la siguiente canción en la cola.
        args:
            ctx (commands.Context): Contexto de discord.
            
        """
        if self.queue:
            audio_url = self.queue.pop()
            await ctx.send("🎶 Reproduciendo...")

            audio_source = discord.FFmpegPCMAudio(audio_url, 
                                            before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", 
                                            executable="C:\\Users\\pc1\\Downloads\\ffmpeg-2025-02-02-git-957eb2323a-full_build\\bin\\ffmpeg.exe")
            ctx.voice_client.play(audio_source, after=lambda e: self.bot.loop.create_task(self.play_next(ctx)))
        else:
            await ctx.send("La cola está vacía.")


    @commands.command()
    async def skip(self, ctx):
        """Salta la canción actual y reproduce la siguiente.
        args:
            ctx (commands.Context): Contexto de discord.
            
        """
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("Canción saltada. Reproduciendo siguiente...")
        else:
            await ctx.send("No estoy reproduciendo ninguna canción.")


    @commands.command()
    async def queue_list(self, ctx):
        """Muestra la lista de canciones en la cola.
        args:
            ctx (commands.Context): Contexto de discord.
            
        """
        if self.queue:
            await ctx.send(f"Lista de canciones en cola:\n" + "\n".join(self.queue.get_queue()))
        else:
            await ctx.send("La cola está vacía.")


async def setup(bot):
    """Añade el cog al bot.
    args:
        bot (commands.Bot): Bot de discord.
        
    """
    await bot.add_cog(Music(bot))
    