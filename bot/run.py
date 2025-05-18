"""Script para ejecutar el bot y el servidor API."""

import subprocess
import sys
import os

def run_services():
    """Ejecuta el bot y el servidor API en procesos separados."""
    # Obtener el directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Ejecutar el servidor API
    api_process = subprocess.Popen([sys.executable, os.path.join(current_dir, 'api_server.py')])
    
    # Ejecutar el bot
    bot_process = subprocess.Popen([sys.executable, os.path.join(current_dir, 'main.py')])
    
    try:
        # Esperar a que ambos procesos terminen
        api_process.wait()
        bot_process.wait()
    except KeyboardInterrupt:
        # Manejar la interrupción del teclado (Ctrl+C)
        print("\nDeteniendo servicios...")
        api_process.terminate()
        bot_process.terminate()
        api_process.wait()
        bot_process.wait()
        print("Servicios detenidos.")

if __name__ == "__main__":
    run_services() 