import json
import unittest
from app import app
from falcon import testing
from route_description import RouteName
from constants import Constants

class TestAddResource(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.test_client = testing.TestClient(self.app)

    def test_addition(self):
        expected_result = 7
        req_body = {"num1": 3, "num2": 4}
        expected_resp_body = {"result": expected_result}

        resp = self.test_client.simulate_post(RouteName.ADD, json=req_body)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json.loads(resp.content), expected_resp_body)

        with open(Constants.PERSISTENCE_STORAGE_PATH, "r") as f:
            contents = f.read()
        self.assertIn("3,4,7", contents)


if __name__ == '__main__':
    unittest.main()
