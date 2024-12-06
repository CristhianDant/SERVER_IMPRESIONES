
from fastapi import APIRouter, Body , Depends , Path , Query , status
from pydantic import BaseModel
from typing import Dict, Any

from fastapi.responses import JSONResponse
from middlewares.JWT_bearer import JWTBearer

from .tiketera.pedidos import Pedidos_Tiketera


router_impresion = APIRouter()


@router_impresion.post("/impresion" , tags=['Impresiones'] ,status_code=status.HTTP_201_CREATED , dependencies=[Depends(JWTBearer())])
def get_impresiones():
    """
    Listar todas las impresiones
    """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Impresiones"}
    )

@router_impresion.post("/impresion_pedido/" , tags=['Impresiones'] ,status_code=status.HTTP_200_OK , dependencies=[Depends(JWTBearer())])
def get_impresiones_pedido(body: Dict[str, Any] = Body(...)):
    """
    Listar todas las impresiones
    """
    
    ip = body.get('ip')
    data = body.get('data')

    result = Pedidos_Tiketera.impresion(ip, data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )
    