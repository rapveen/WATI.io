import falcon
from wsgiref.simple_server import make_server
from add_resource import AddResource
from route_description import RouteName


app = falcon.App()
app.add_route(RouteName.ADD, AddResource())


if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8080, app)
    httpd.serve_forever()
