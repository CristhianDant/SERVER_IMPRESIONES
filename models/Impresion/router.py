from fastapi import APIRouter, Body , Depends , Path , Query , status
from pydantic import BaseModel
from typing import Dict, Any

from fastapi.responses import JSONResponse
from middlewares.JWT_bearer import JWTBearer

from .tiketera.pedidos import Pedidos_Tiketera
from .tiketera.caja import Caja_Tiketera
from .tiketera.factura import Factura_Tiketera
from .tiketera.devolucion import Devolucion_Tiketera
from .tiketera.guia_interna_amp import GuiaInternaAmp
from .tiketera.compra_apt import Compra_apt


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
    Generar la impresion de pedidos
    """
    
    ip = body.get('ip')
    data = body.get('data')

    result = Pedidos_Tiketera.impresion(ip, data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )
    

@router_impresion.post('/impresion_caja/' , tags=['Impresiones'] , status_code=status.HTTP_200_OK , dependencies=[Depends(JWTBearer())])
def get_impresiones_caja(boby :Dict[str , Any ] = Body(...)):
    """
    Generar la impresion de caja     
    """ 

    ip = boby.get('ip')
    data = boby.get('data')

    result = Caja_Tiketera.impresion(ip=ip , data = data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )

@router_impresion.post('/impresion_factura/' , tags=['Impresiones'] , status_code=status.HTTP_200_OK , dependencies=[Depends(JWTBearer())])
def get_impresiones_factura(boby :Dict[str , Any ] = Body(...)):
    """
    Generar la impresion de factura
    """ 

    ip = boby.get('ip')
    data = boby.get('data')

    result = Factura_Tiketera.impresion(ip=ip , data = data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )

@router_impresion.post('/impresion_devolucino/' , tags=['Impresiones'] , status_code=status.HTTP_200_OK , dependencies=[Depends(JWTBearer())])
def get_impresiones_devolucion(boby :Dict[str , Any ] = Body(...)):
    """
    Generar la impresion de devolucion
    """ 

    ip = boby.get('ip')
    data = boby.get('data')

    result = Devolucion_Tiketera.impresion(ip=ip , data = data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )

@router_impresion.post('/impresion_guia_interna_amp/' , tags=['Impresiones'] , status_code=status.HTTP_200_OK , dependencies=[Depends(JWTBearer())])
def get_impresiones_guia_interna_amp(boby :Dict[str , Any ] = Body(...)):
    """
    Generar la impresion de guia interna amp
    """

    ip = boby.get('ip')
    data = boby.get('data')

    result = Compra_apt.impresion(ip=ip, data = data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )

@router_impresion.post('/compra_apt/' , tags=['Impresiones'] , status_code=status.HTTP_200_OK , dependencies=[Depends(JWTBearer())])
def get_impresiones_compra_apt(boby :Dict[str , Any ] = Body(...)):
    """
    Generar la impresion de compra apt
    """

    ip = boby.get('ip')
    data = boby.get('data')

    result = Compra_apt.impresion(ip=ip, data = data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=result
    )
