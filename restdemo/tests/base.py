import unittest

from restdemo import db, create_app


class TestBase(unittest.TestCase):

    # 搭建測試環境
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()            # 模擬客戶端
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.user_data = {
            "username": "test",
            "password": "test123",
            "email": "test@test.com"
        }

        # set 內存 DB table
        db.create_all()

    # 刪除測試環境
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        if self.app_context is not None:
            self.app_context.pop()
