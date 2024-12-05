from fastapi import APIRouter, Body , Depends , Path , Query , status
from fastapi.responses import JSONResponse

from database.db import Session
from .model import Printer
from .servise import PrinterService

# Crear un router

printer_router = APIRouter()

@printer_router.get("/printer" , tags=['Impresoras'] 
    ,status_code=status.HTTP_200_OK
)
def get_printers():
    """
    Listar todas las impresoras
    """
    db = Session()
    result = PrinterService(db).get_printers()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )
    

@printer_router.get("/register" , tags=['Impresoras']
    ,status_code=status.HTTP_201_CREATED
)
def register_printer_tickers():
    """
    Registrar impresoras de tickets
    """
    db = Session()
    PrinterService(db).reguister_printer_tickers()
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Impresoras registradas"}
    )

@printer_router.get("/printer/{id}" , tags=['Impresoras']
    ,status_code=status.HTTP_200_OK
)
def get_printer(id: int = Path(..., title="ID de la impresora")):
    """
    Obtener una impresora por ID
    """
    db = Session()
    result = PrinterService(db).get_printer(id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )

    
