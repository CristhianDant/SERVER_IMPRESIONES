import os 
from dotenv import load_dotenv
from fastapi import HTTPException


from jwt import decode , encode
from datetime import datetime, timedelta , timezone
from jwt import decode, ExpiredSignatureError, InvalidTokenError 
from typing import Dict, Any
load_dotenv()

key = os.getenv('SECRET_KEY')


def create_token(data: dict, expires_in: int = 1) -> str:
    """
    Crea un token JWT con un tiempo de expiración.

    :param data: Datos a incluir en el payload del token.
    :param expires_in: Tiempo de expiración en minutos (por defecto 60 minutos).
    :return: Token JWT como una cadena.
    """
    expiration = datetime.now(timezone.utc)+ timedelta(minutes=expires_in)
    data.update({"exp": expiration})
    token = encode(payload=data, key=key, algorithm="HS256")
    return token

def validate_token(token: str) -> Dict[str, Any]:
    try:
        data = decode(jwt=token, key=key, algorithms=["HS256"])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    data = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": 1516239022
    }
    token = create_token(data)
    print(token)
    #token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE3MzQxMjk1MTF9.xJaKeZtB1ABKWB6gX-Ve9V4jUliHN23bePfglIV2yhM'
    print(validate_token(token))
