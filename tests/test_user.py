import unittest
from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password = 'agnes1234')

    def test_init(self):
        self.assertTrue(self.new_user.password_encrypt is not None)

    def test_alert(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_save(self):
        self.assertTrue(self.new_user.check_password('agnes1234'))