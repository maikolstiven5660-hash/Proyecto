from fastapi import FastAPI
from metodos import consultarApi
from database import engine
from modelos import model_producto

model_producto.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(consultarApi.router, prefix="/productos")