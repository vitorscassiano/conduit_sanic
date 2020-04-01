from sanic import Blueprint
from sanic.response import json
from sanic.log import logger
from asyncio import sleep
from random import randint

blueprint = Blueprint("Healthcheck", "/")

@blueprint.get("/status")
async def status(request):
    await sleep(randint(0, 5))
    return json({
        "message": "After this heavy overload, I'm Ok Dude!",
        "status": 200
    })


@blueprint.get("/healthcheck")
async def healthcheck(request):
    return json({
        "message": "After this heavy overload, I'm Ok Dude!",
        "status": 200
    })
