
import os


class path:
    root = os.path.dirname(os.path.abspath(__file__))

    input_path = os.path.join(root,'input')

    cogs_path = os.path.join(root, 'cogs')

    utils_path = os.path.join(root, 'utils')

    ffpeg_local_path = root + '\\..\\ffmpeg\\bin\\ffmpeg.exe'

    routers = os.path.join(root, 'router')
