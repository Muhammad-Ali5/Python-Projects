import unittest
from src.login import login

class TestLogin(unittest.TestCase):
    # 4 Positive Test Cases
    def test_login_standard_user(self):
        self.assertTrue(login('user', 'pass'), "Standard user should be able to login")

    def test_login_admin_user(self):
        self.assertTrue(login('admin', 'admin123'), "Admin user should be able to login")

    def test_login_guest_user(self):
        self.assertTrue(login('guest', 'guest'), "Guest user should be able to login")
        
    def test_login_test_user(self):
        self.assertTrue(login('test', 'test'), "Test user should be able to login")

    # 2 Negative Test Cases
    def test_invalid_username(self):
        self.assertFalse(login('invalid_user', 'pass'), "Invalid username should fail")

    def test_invalid_password(self):
        self.assertFalse(login('user', 'wrong_pass'), "Invalid password should fail")

if __name__ == '__main__':
    unittest.main()
