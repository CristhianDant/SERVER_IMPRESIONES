from fastapi import APIRouter, Body , Depends, HTTPException , Path , Query , status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from database.db import Session
from .model import Printer_database
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
        content=jsonable_encoder(result)
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
        content=jsonable_encoder(result)    
    )
@printer_router.put("/printer_name/" , tags=['Impresoras']
    ,status_code=status.HTTP_200_OK
)
def update_printer_name(body: dict = Body(... , examples=[{
    'id': 1,
    "name": "Nombre de la impresora"
}])):
    """
    Actualizar el nombre de la impresora
    """
    db = Session()
    

    if not 'id' in body or not 'name' in body:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Faltan parametros"}
        )
    

    result = PrinterService(db).update_name_printer(body['id'], body['name'])
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Impresora no encontrada")

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(result)
    )
    
    
