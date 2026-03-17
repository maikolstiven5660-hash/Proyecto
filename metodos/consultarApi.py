from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from modelos import model_producto
from esquemas import eschemas

router = APIRouter()

# GET - Consultar todos los productos
@router.get("/")
async def consultar():
    return "Consultar productos..."

@router.get("/prod_all")
def get_productos(db: Session = Depends(get_db)):
    productos = db.query(model_producto.Producto).all()
    return productos

# GET - Consultar un producto por ID
@router.get("/prod/{prodId}")
def get_producto(prodId: int, db: Session = Depends(get_db)):
    producto = db.query(model_producto.Producto).filter(
        model_producto.Producto.id_prod == prodId).first()
    if producto:
        return producto
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# POST - Crear un producto
@router.post("/add", response_model=eschemas.Producto)
def crear_producto(producto: eschemas.Producto, db: Session = Depends(get_db)):
    nuevo = model_producto.Producto(
        id_prod=producto.id_prod,
        nom_prod=producto.nom_prod,
        proveedor=producto.proveedor
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# PUT - Actualizar un producto
@router.put("/update/{id_prod}", response_model=eschemas.Producto)
def update_producto(id_prod: int, producs: eschemas.Producto, db: Session = Depends(get_db)):
    producto = db.query(model_producto.Producto).filter(
        model_producto.Producto.id_prod == id_prod).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto.id_prod = producs.id_prod
    producto.nom_prod = producs.nom_prod
    producto.proveedor = producs.proveedor
    db.commit()
    db.refresh(producto)
    return producto

# DELETE - Borrar un producto
@router.delete("/borrar/{id_prod}")
def borrar_producto(id_prod: int, db: Session = Depends(get_db)):
    producto = db.query(model_producto.Producto).filter(
        model_producto.Producto.id_prod == id_prod).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"detail": "Producto eliminado"}