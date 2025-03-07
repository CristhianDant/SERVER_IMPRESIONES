# env 
# SECRET_KEY = 'your_secret_key'

from fastapi import FastAPI 
from fastapi.responses import RedirectResponse

from models.Networth_Printer import Networth_Printer
from database.db import engine , Base

app = FastAPI()
app.title = "Impresoras Server API"
app.description = "API para la gestión de impresoras en red"

## add_middleware
from middlewares.Error_handler import ErrorHandler
app.add_middleware(ErrorHandler)

## Import routers
from models.Impresoras.router import printer_router
app.include_router(printer_router)

from models.Impresion.router import router_impresion
app.include_router(router_impresion)

# Crear la base de datos 
Base.metadata.create_all(bind=engine)

SECRET_KEY = 'your_secret_key'

@app.get("/" , tags=["Root"])
def read_root():
    """
    Este endpoint redirige a la documentación de la API
    """
    return RedirectResponse(url="/docs")


"""
Para la ejecucion de este servidor se usa uvicorn
uvicorn main:app --host 0.0.0.0 --port 8080 --reload 
"""