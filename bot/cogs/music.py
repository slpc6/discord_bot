"""Clase que contiene el modulo de música para el bot de Discord."""

#External libraries
import discord
import os
import yt_dlp

from discord.ext import commands

#Ouwn libraries
from utils.audio_queue import AudioQueue
from path import path

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
            await ctx.send("LLEGUE YO HIJUEPUTAAAAAA.")
        else:
            await ctx.send("El burro por delante.")


    @commands.command()
    async def leave(self, ctx):
        """El bot sale del canal de voz.
        args:
            ctx (commands.Context): Contexto de discord.
            
        """
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Suerte gonorreas 😈")
        else:
            await ctx.send("No estoy en el canal de voz, me estoy culiando a su madre.")


    @commands.command()
    async def play(self, ctx, *, query: str):
        """Agrega una canción a la cola y reproduce.
        args:
            ctx (commands.Context): Contexto de discord.
            query: URL de la canción.
            
        """
        if not ctx.voice_client:
            await ctx.invoke(self.join)
        
        await ctx.send("🎵 Cargando el tema...")
        file_path = os.path.join(path.input_path, 'cookie.txt')

        ydl_opts = {
            'format': 'bestaudio',
            'quiet': True,
            'default_search': 'ytsearch',
            'noplaylist': True,
            'cookies': file_path,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            
            if 'entries' in info:
                video = info['entries'][0]
                audio_url = video['url']
                title = video['title']
            else:
                await ctx.send("Escriba bien gonorrea, eso no aparece malparido.")
                return

        self.queue.add(audio_url)
        await ctx.send(f"🎶 {title} Guardelo ahi que ya le suena.")

        if not ctx.voice_client.is_playing():
            await self.play_next(ctx)


    async def play_next(self, ctx):
        """Reproduce la siguiente canción en la cola.
        args:
            ctx (commands.Context): Contexto de discord.
            
        """
        if not self.queue.is_empty():
            audio_url = self.queue.pop()
            await ctx.send("🎶 Reproduciendo...")

            audio_source = discord.FFmpegPCMAudio(audio_url, 
                                            before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                                            executable=path.ffpeg_local_path
                                            )
            ctx.voice_client.play(audio_source, after=lambda e: self.bot.loop.create_task(self.play_next(ctx)))
        else:
            await ctx.send("Lleneme mas la cola, no pare por favor! UWU")


    @commands.command()
    async def skip(self, ctx):
        """Salta la canción actual y reproduce la siguiente.
        args:
            ctx (commands.Context): Contexto de discord.
            
        """
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("Tema pa maluco no (?)")
        else:
            await ctx.send("Pero haceme debutar primero.")


    @commands.command()
    async def queue_list(self, ctx):
        """Muestra la lista de canciones en la cola.
        args:
            ctx (commands.Context): Contexto de discord.
            
        """
        if not self.queue.is_empty():
            await ctx.send(f"Las que se viene pal soye:\n" + "\n".join(self.queue.get_queue()))
        else:
            await ctx.send("Lleneme mas la cola, no pare por favor! UWU")


async def setup(bot):
    """Añade el cog al bot.
    args:
        bot (commands.Bot): Bot de discord.
        
    """
    await bot.add_cog(Music(bot))
    