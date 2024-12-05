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


# Crear la base de datos 
Base.metadata.create_all(bind=engine)


@app.get("/" , tags=["Root"])
def read_root():
    """
    Este endpoint redirige a la documentación de la API
    """
    return RedirectResponse(url="/docs")