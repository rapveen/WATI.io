import json
import unittest
from app import app
from falcon import testing
from route_description import RouteName

class TestAddResource(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.test_client = testing.TestClient(self.app)

    def test_addition(self):
        expected_result = 5
        req_body = {"num1": 2, "num2": 3}
        expected_resp_body = {"result": expected_result}

        resp = self.test_client.simulate_post(RouteName.ADD, json=req_body)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.content), expected_resp_body)


if __name__ == '__main__':
    unittest.main()
