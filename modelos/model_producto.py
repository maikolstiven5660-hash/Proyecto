from sqlalchemy import Column, Integer, String
from database import Base

class Producto(Base):
    __tablename__ = "producto"
    
    id_prod = Column(Integer, primary_key=True, index=True)
    nom_prod = Column(String(100))
    proveedor = Column(String(150))