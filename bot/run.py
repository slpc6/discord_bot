"""Script para ejecutar el bot y el servidor API."""

import subprocess
import sys
import os
import asyncio
from utils.api_poller import APIPoller
from dotenv import load_dotenv


async def run_services():
    """Ejecuta el bot, el servidor API y el poller en procesos separados."""
    # Obtener el directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Ejecutar el servidor API
    api_process = subprocess.Popen([sys.executable, os.path.join(current_dir, 'api_server.py')])
    
    # Ejecutar el bot
    bot_process = subprocess.Popen([sys.executable, os.path.join(current_dir, 'main.py')])
    
    # Iniciar el APIPoller
    api_poller = APIPoller("http://localhost:8000")  # Ajusta la URL según tu API
    poller_task = asyncio.create_task(api_poller.start())
    
    try:
        # Esperar a que ambos procesos terminen
        await asyncio.gather(
            asyncio.to_thread(api_process.wait),
            asyncio.to_thread(bot_process.wait)
        )
    except KeyboardInterrupt:
        # Manejar la interrupción del teclado (Ctrl+C)
        print("\nDeteniendo servicios...")
        api_process.terminate()
        bot_process.terminate()
        api_poller.stop()
        poller_task.cancel()
        await asyncio.gather(
            asyncio.to_thread(api_process.wait),
            asyncio.to_thread(bot_process.wait),
            poller_task,
            return_exceptions=True
        )
        print("Servicios detenidos.")


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(run_services()) 
