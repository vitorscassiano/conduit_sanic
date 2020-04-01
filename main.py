from sanic import Sanic
from sanic.response import json
from sanic.log import logger

from conduit.blueprints.product import blueprint as product_blueprint
from conduit.blueprints.healthcheck import blueprint as healthcheck_blueprint
from conduit.middlewares import (
    request_time,
    response_time,
    generate_request_id
)

from conduit.settings import (
    HOST,
    PORT
)

app = Sanic()

# Blueprints
app.register_blueprint(healthcheck_blueprint)
app.register_blueprint(product_blueprint)

# Middlewares
app.register_middleware(generate_request_id, attach_to="request")
app.register_middleware(request_time, attach_to="request")
app.register_middleware(response_time, attach_to="response")


def main():
    app.run(host=HOST, port=PORT)


if __name__ == "__main__":
    main()
