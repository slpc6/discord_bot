
import os


class path:
    root = os.path.dirname(os.path.abspath(__file__))

    input_path = os.path.join(root,'input')

    cogs_path = os.path.join(root, 'cogs')

    utils_path = os.path.join(root, 'utils')

    ffpeg_local_path = 'C:\\Users\\pc1\\Downloads\\ffmpeg-2025-02-02-git-957eb2323a-full_build\\bin\\ffmpeg.exe'
