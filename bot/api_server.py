"""Servidor API para el bot de Discord."""

import uvicorn
import markdown2
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI(version="1.0.0", title="Discord bot", description="")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path='/', response_class=HTMLResponse)
def main():
    readme_path = Path(__file__).parent.parent / 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    html_content = markdown2.markdown(markdown_content)
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Discord Bot Documentation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 5px;
                    border-radius: 3px;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
    </html>
    """


@app.get(path='/healthz')
def healthz():
    return JSONResponse({'text': 'OK'}, status_code=200)

if __name__ == "__main__":
    """Punto de inicio del servidor API."""
    uvicorn.run(app="api_server:app", host="0.0.0.0", port=8000, reload=True) 
