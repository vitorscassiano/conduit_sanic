from time import time
from sanic.log import logger
from uuid import uuid4

async def request_time(request):
    request["request_time_start"] = time()


async def response_time(request, response):
    end = time()
    start = request["request_time_start"]
    logger.info(f"The request time was {end - start}/ms")

async def generate_request_id(request):
  request["id"] = uuid4()
