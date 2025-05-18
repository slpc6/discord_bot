# Bot de Discord

Este es un bot de Discord desarrollado en Python utilizando la librería `discord.py`. El bot permite reproducir música desde enlaces de YouTube, gestionar una cola de reproducción, saltar canciones y más.

## Funcionalidades principales

- **Reproducción de música**: El bot puede reproducir música desde enlaces de YouTube.
- **Cola de reproducción**: Las canciones se añaden a una cola y se reproducen en orden.
- **Saltar canciones**: Los usuarios pueden saltar la canción actual y pasar a la siguiente en la cola.
- **Listar la cola**: Muestra las canciones que están en la cola de reproducción.
- **Comandos básicos**: Incluye comandos como `ping` para verificar la latencia del bot.
- **Enviar mensajes predefinidos**: Envia un mensaje aleatorio de una lista de mensajes predefinidos.
- **API REST**: Incluye un servidor API con documentación y endpoint de salud.

## Estructura del proyecto

El proyecto está organizado en módulos para facilitar la escalabilidad y el mantenimiento. A continuación, se describe la estructura de archivos y carpetas:

```
bot/
│
├── main.py # Punto de entrada del bot
├── api_server.py # Servidor API con documentación
├── run.py # Script para ejecutar el bot y el servidor API
├── cogs/ # Carpeta para los módulos de comandos (cogs)
│   ├── music.py # Módulo para comandos de música
│   └── general.py # Módulo para comandos generales (ping, etc.)
├── utils/ # Carpeta para utilidades
│   └── audio_queue.py # Módulo para manejar la cola de reproducción
└── config.py # Configuración del bot (token, prefijo, etc.)
```

### `main.py`

Es el punto de entrada del bot. Aquí se configura el bot y se cargan los módulos (cogs). También se maneja el evento `on_ready`, que se ejecuta cuando el bot se conecta correctamente a Discord.

### `api_server.py`

Contiene el servidor API desarrollado con FastAPI que proporciona:
- Documentación del bot en la ruta raíz ('/')
- Endpoint de salud en '/healthz'

### `run.py`

Script que ejecuta tanto el bot como el servidor API en procesos separados para evitar conflictos con el event loop de asyncio.

### `cogs/`

Contiene los módulos de comandos. Cada módulo es una clase que hereda de `commands.Cog` y agrupa comandos relacionados.

- **`general.py`**: Contiene comandos generales como `ping`.
- **`music.py`**: Contiene todos los comandos relacionados con la reproducción de música, como `play`, `skip`, `queue_list`, etc.
- **`copypaste.py`**: Contiene los comandos para generar un copy paste aleatorio.

### `utils/`

Contiene utilidades que pueden ser reutilizadas en diferentes partes del bot.

- **`audio_queue.py`**: Maneja la cola de reproducción de música. Implementa una cola FIFO (First In, First Out) utilizando `deque` de la librería `collections`.

### `config.py`

Contiene la configuración del bot, como el token de Discord y el prefijo de comandos. Las variables de entorno se cargan desde un archivo `.env`.

## Comandos disponibles

### Comandos generales

- **`$ping`**: Responde con "¡Pong!" para verificar que el bot está funcionando.

### Comandos de música

- **`$join`**: El bot se une al canal de voz del usuario.
- **`$leave`**: El bot sale del canal de voz.
- **`$play <url>`**: Reproduce una canción desde un enlace de YouTube. Si ya hay una canción en reproducción, la nueva canción se añade a la cola.
- **`$skip`**: Salta la canción actual y reproduce la siguiente en la cola.
- **`$queue_list`**: Muestra la lista de canciones en la cola de reproducción.

## API Endpoints

- **`GET /`**: Muestra la documentación del bot en formato HTML.
- **`GET /healthz`**: Endpoint de salud que devuelve el estado del servidor.

## Requisitos

Para ejecutar el bot, necesitas:

- Python 3.8 o superior.
- Las siguientes librerías de Python:
  - `discord.py`
  - `yt-dlp`
  - `python-dotenv`
  - `fastapi`
  - `uvicorn`
  - `markdown2`

Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el bot y el servidor API:

```bash
python bot/run.py
```

Esto iniciará:
- El servidor API en `http://localhost:8000`
- El bot de Discord

Para detener ambos servicios, presiona `Ctrl+C` en la terminal.
