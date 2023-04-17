import falcon
from falcon_cors import CORS
from wsgiref.simple_server import make_server
from resources.add_resource import AddResource
from resources.index_resource import IndexResource
from route_description import RouteName


app = falcon.App()
cors = CORS(allow_all_origins=True)
app.add_middleware(cors.middleware)
app.add_route(RouteName.INDEX, IndexResource())
app.add_route(RouteName.ADD, AddResource())


if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8080, app)
    httpd.serve_forever()
