"""Funcion que cargar un texto desde un archivo de texto ubicado en la carpeta input/"""

import os

def text_loader(archivo: str) -> list:
    file_path = f'../bot/input/{archivo}'
    with open(file_path, 'r', encoding='utf-8') as file:
        textos = [linea.strip() for linea in file]
        return textos