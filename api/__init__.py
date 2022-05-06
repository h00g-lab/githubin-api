from flask_restx import Api

from .helloworld import api as hello_api
from .thirdparty import api as thirdparty_api

api = Api(title="Githubin", version="beta", description="Rapidin de mais",)

api.add_namespace(hello_api)
api.add_namespace(thirdparty_api)