"""Funcion que cargar un texto desde un archivo de texto ubicado en la carpeta input/"""

import os
from path import path

def text_loader(archivo: str) -> list:

    input_path = path.input_path
    file_path = os.path.join(input_path, archivo)
    with open(file_path, 'r', encoding='utf-8') as file:
        textos = [linea.strip() for linea in file]
        return textos
    