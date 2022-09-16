import json

from restdemo.tests.base import TestBase


class TestUser(TestBase):

    def test_user_create(self):
        url = '/user/{}'.format(self.user_data["username"])
        res = self.client.post(
            url,
            data=json.dumps(self.user_data),
            headers={"Content-Type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res_data.get("username"), self.user_data["username"])
        self.assertEqual(res_data["email"], self.user_data["email"])

        res = self.client.post(
            url,
            json=self.user_data
        )
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res_data.get("message"), "user already exist")

    def test_user_get(self):
        url = '/user/{}'.format(self.user_data["username"])
        res = self.client.post(
            url,
            json=self.user_data
        )
        res = self.client.get(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data["username"], self.user_data["username"])
        self.assertEqual(res_data["email"], self.user_data["email"])

    def test_user_get_not_exist(self):
        url = '/user/{}'.format(self.user_data["username"])
        res = self.client.get(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {"message": "user not found"})

    def test_user_delete(self):
        url = '/user/{}'.format(self.user_data["username"])
        res = self.client.post(
            url,
            json=self.user_data
        )
        res = self.client.delete(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data, {"message": "user deleted"})

    def test_user_delete_not_exist(self):
        url = '/user/{}'.format(self.user_data["username"])
        res = self.client.delete(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {"message": "user not found"})

    def test_user_update(self):
        url = '/user/{}'.format(self.user_data["username"])
        res = self.client.post(
            url,
            json=self.user_data
        )
        res = self.client.put(
            url,
            json={
                "password": "newpassword",
                "email": "newemail@new.com"
            }
        )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data["email"], "newemail@new.com")

    def test_user_update_not_exist(self):
        url = '/user/{}'.format(self.user_data["username"])
        res = self.client.put(
            url,
            json={
                "password": "newpassword",
                "email": "newemail@new.com"
            }
        )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {"message": "user not found"})
