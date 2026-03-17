from fastapi import FastAPI
from metodos import consultarApi

app = FastAPI()

app.include_router(consultarApi.router, prefix="/productos")