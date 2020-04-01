from sanic import Blueprint
from sanic.response import json
from sanic.log import logger
from conduit.services.user import User

blueprint = Blueprint("User", "/v1/users")
database = {
    "d0fa60f9-c1f1-4bea-9e3b-7ba0ea1ae519": {
        "id": "d0fa60f9-c1f1-4bea-9e3b-7ba0ea1ae519",
        "name": "Faker",
        "email": "faker@gmail.com",
        "password": "xpto",
        "createdAt": "2020-04-01T13:16:50.161420"
    }
}


@blueprint.get("/<id>")
async def get_users(request, id):
    logger.info(f"The id is: {id} for the database: {database}")
    user = User(database).find(id)
    return json(user)


@blueprint.post("/")
async def create_users(request):
    payload = request.json
    user = User(database).create(payload)

    return json(user)


@blueprint.delete("/<id>")
async def delete_users(request, id):
    check = User(database).delete(id)

    return json({"message": f"deleted was {check}"})
