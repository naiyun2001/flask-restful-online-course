import json

from restdemo.tests.base import TestBase

class TestUser(TestBase):

    def test_login(self):
        url = '/user/{}'.format(self.user_data["username"])
        res = self.client.post(
            url, 
            json = self.user_data
        )
        
        url = "/auth/login"
        res = self.client.post(
            url,
            # json = {
            #     "username": "test",
            #     "password": "test123"
            # }
            data = json.dumps({"username": "test","password": "test123"}),
            headers = {"Content-Type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertIn("access_token", res_data)

    def test_login_filed(self):
        url = '/user/{}'.format(self.user_data["username"])
        res = self.client.post(
            url, 
            json = self.user_data
        )
        
        url = "/auth/login"
        res = self.client.post(
            url,
            json = {
                "username": "test",
                "password": "wrongpwd"
            }
        )
        self.assertEqual(res.status_code, 401)
        res_data = json.loads(res.get_data(as_text=True))
        data = {
            "description": "Invalid credentials",
            "error": "Bad Request",
            "status_code": 401
        }
        self.assertEqual(res_data, data)