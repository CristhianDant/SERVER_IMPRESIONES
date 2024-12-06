from fastapi import APIRouter, Body , Depends , Path , Query , status
from fastapi.responses import JSONResponse

from middlewares.JWT_bearer import JWTBearer
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
