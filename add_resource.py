# request format
# req.context['request_body'] = {
#     "num1": 323,
#     "num2": 344
# }

# resp.body = HTTP status code
# resp.response_body = {}

import falcon
import json
from constants import Constants


class AddResource(object):
    def __init__(self):
        self.persistence_storage_path = Constants.PERSISTENCE_STORAGE_PATH

    def on_post(self, req, resp):
        # req_body = req.context.get("request_body")
        # print(req.context)
        num1 = req.media["num1"]
        num2 = req.media["num2"]
        result = num1+num2

        with open(self.persistence_storage_path, "a") as f:
            f.write(f"{num1},{num2},{result}\n")

        resp.body = json.dumps({"result": result})
        resp.status = falcon.HTTP_200

