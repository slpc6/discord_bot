"""Clase para el manejo de imágenes y videos en el bot de discord."""

#External libraries
from discord.ext import commands
import discord
import os
import random
from path import path


class Picture(commands.Cog):
    """Clase para el manejo de imágenes y videos en el bot de discord."""


    def __init__(self, bot):
        """Inicializa el bot.
        args:
            bot (commands.Bot): Bot de discord.
        """
        self.bot = bot
        self.media_path = os.path.join(path.input_path, 'media')
        self.media_path_lol = os.path.join(path.input_path, 'Lol')
        self.image_extensions = ('.png', '.jpg', '.jpeg', '.gif')
        self.video_extensions = ('.mp4', '.mov', '.avi', '.mkv', '.webm')


    def get_files_recursively(self, directory, extensions):
        """Obtiene archivos recursivamente desde un directorio y sus subdirectorios.
        args:
            directory (str): Directorio base para la búsqueda
            extensions (tuple): Extensiones de archivo a buscar
        returns:
            list: Lista de rutas completas de archivos encontrados
        """
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.lower().endswith(extensions):
                    files.append(os.path.join(root, filename))
        return files


    def get_media_files(self, media_type='image'):
        """Obtiene la lista de archivos según el tipo de medio.
        args:
            media_type (str): Tipo de medio ('image' o 'video')
        returns:
            list: Lista de archivos del tipo especificado
        """
        if media_type == 'lol':
            extensions = self.video_extensions
            return self.get_files_recursively(self.media_path_lol, extensions)
        else:
            extensions = self.image_extensions if media_type == 'image' else self.video_extensions
            return self.get_files_recursively(self.media_path, extensions)


    @commands.command()
    async def image(self, ctx):
        """Envía una imagen aleatoria del directorio de medios.
        args:
            ctx (commands.Context): Contexto del comando.
        """
        try:
            images = self.get_media_files('image')
            
            if not images:
                await ctx.send("No hay imágenes disponibles en el directorio.")
                return
            
            random_image = random.choice(images)
            
            # Enviar la imagen
            with open(random_image, 'rb') as f:
                await ctx.send(file=discord.File(f, filename=os.path.basename(random_image)))
            
        except Exception as e:
            await ctx.send(f"Error al enviar la imagen: {str(e)}")


    @commands.command()
    async def video(self, ctx):
        """Envía un video aleatorio del directorio de medios.
        args:
            ctx (commands.Context): Contexto del comando.
        """
        try:
            videos = self.get_media_files('video')
            
            if not videos:
                await ctx.send("No hay videos disponibles en el directorio.")
                return
            
            random_video = random.choice(videos)
            
            # Enviar el video
            with open(random_video, 'rb') as f:
                await ctx.send(file=discord.File(f, filename=os.path.basename(random_video)))
            
        except Exception as e:
            await ctx.send(f"Error al enviar el video: {str(e)}")


    @commands.command()
    async def videolol(self, ctx):
        """Envía un video aleatorio del directorio de medios.
        args:
            ctx (commands.Context): Contexto del comando.
        """
        try:
            videos = self.get_media_files('lol')
            
            if not videos:
                await ctx.send("No hay videos disponibles en el directorio.")
                return
            
            random_video = random.choice(videos)
            
            # Enviar el video
            with open(random_video, 'rb') as f:
                await ctx.send(file=discord.File(f, filename=os.path.basename(random_video)))
            
        except Exception as e:
            await ctx.send(f"Error al enviar el video: {str(e)}")


    @commands.command()
    async def media(self, ctx, media_name: str):
        """Envía un archivo multimedia específico por nombre.
        args:
            ctx (commands.Context): Contexto del comando.
            media_name (str): Nombre del archivo a enviar.
        """
        try:
            # Buscar el archivo con el nombre proporcionado
            media_found = None
            for root, _, filenames in os.walk(self.media_path):
                for filename in filenames:
                    if filename.lower().startswith(media_name.lower()) and \
                       (filename.lower().endswith(self.image_extensions) or 
                        filename.lower().endswith(self.video_extensions)):
                        media_found = os.path.join(root, filename)
                        break
                if media_found:
                    break
            
            if not media_found:
                await ctx.send(f"No se encontró ningún archivo que comience con '{media_name}'")
                return
            
            # Enviar el archivo
            with open(media_found, 'rb') as f:
                await ctx.send(file=discord.File(f, filename=os.path.basename(media_found)))
            
        except Exception as e:
            await ctx.send(f"Error al enviar el archivo: {str(e)}")


async def setup(bot):
    """Añade el cog al bot.
    args:
        bot (commands.Bot): Bot de discord.
    """
    await bot.add_cog(Picture(bot))