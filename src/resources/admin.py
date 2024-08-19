import logging
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.response import Response
from pyconman import ConfigLoader

config = ConfigLoader.get_config()
logger = logging.getLogger(config.get("service"))

from services.products_service import get_all_products

# Create an APIRouter instance
admin_router = APIRouter()

@admin_router.get('/products')
async def all_products():
    logger.info("Get admin products.")
    products = get_all_products()
    logger.debug("Retrieved products successfully.")
    resp = Response(True, "All products.", products)
    return JSONResponse(content=resp.to_dict())
