from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response , status
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            print(e)
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={'error': str(e)})