import os 
from dotenv import load_dotenv

from jwt import decode , encode
load_dotenv()

key = os.getenv('SECRET_KEY')


def create_token(data: dict) -> str:
    token = encode(payload=data, key=key, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    try:
        #print(token)
        data = decode(jwt=token, key=key, algorithms=["HS256"])
        return data
    except Exception as e:
        raise e

if __name__ == "__main__":
    data = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": 1516239022
    }
    token = create_token(data)
    print(token)
    print(validate_token(token))
