from sanic import Blueprint
from sanic.response import json
from sanic.log import logger
from conduit.services.product import Product

blueprint = Blueprint("Product", "/v1/products")
database = {
    "89dcb24c-e493-4a32-bdf3-423a1ecb839f": {
        "id": "89dcb24c-e493-4a32-bdf3-423a1ecb839f",
        "name": "Fake name",
        "description": "Sample Description",
        "createdAt": "2020-04-01T13:16:50.161420"
    }
}


@blueprint.get("/")
async def list_products(request):
    products = Product(database).find()
    return json(products)


@blueprint.get("/<id>")
async def list_products(request, id):
    logger.info(f"The id is: {id} for the database: {database}")
    products = Product(database).find(id)
    return json(products)


@blueprint.post("/")
async def create_products(request):
    payload = request.json
    product = Product(database).create(payload)

    return json(product)


@blueprint.delete("/<id>")
async def delete_products(request, id):
    check = Product(database).delete(id)

    return json({"message": f"deleted was {check}"})
