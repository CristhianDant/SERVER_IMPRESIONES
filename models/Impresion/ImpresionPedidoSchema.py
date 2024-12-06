from pydantic import BaseModel, Field
from typing import Dict, Any

class ImpresionPedidoSchema(BaseModel):
    ip: str = Field(..., example="467.990.234.768")
    data: Dict[str, Any] = Field(..., example={})

    class Config:
        json_schema_extra = {
            "example": {
                "ip": "467.990.234.768",
                "data": {
                    "key1": "value1",
                    "key2": "value2"
                }
            }
        }