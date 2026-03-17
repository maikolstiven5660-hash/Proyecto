from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id_prod: Optional[int] = None
    nom_prod: str
    proveedor: str

    class Config:
        from_attributes = True