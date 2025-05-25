"""Módulo para realizar peticiones periódicas a la API."""

import asyncio
import aiohttp
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class APIPoller:
    def __init__(self, api_url: str, interval: int = 60):
        """
        Inicializa el poller de la API.
        
        Args:
            api_url (str): URL de la API a la que se harán las peticiones
            interval (int): Intervalo en segundos entre peticiones (default: 60)
        """
        self.api_url = api_url
        self.interval = interval
        self.is_running = False

    async def check_api(self):
        """Realiza una petición a la API y verifica la respuesta."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url) as response:
                    if response.status == 200:
                        logger.info(f"API check successful at {datetime.now()}")
                    else:
                        logger.warning(f"API check failed with status {response.status} at {datetime.now()}")
        except Exception as e:
            logger.error(f"Error checking API: {str(e)}")

    async def start(self):
        """Inicia el proceso de polling."""
        self.is_running = True
        while self.is_running:
            await self.check_api()
            await asyncio.sleep(self.interval)

    def stop(self):
        """Detiene el proceso de polling."""
        self.is_running = False 