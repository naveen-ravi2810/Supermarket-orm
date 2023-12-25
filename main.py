from fastapi import FastAPI

from Api.endpoint_v1.Products import router as product_router

app = FastAPI()

app.include_router(product_router, prefix='/product')
