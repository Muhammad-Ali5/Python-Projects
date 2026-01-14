import unittest
from src.login import login

class TestLoginIntegration(unittest.TestCase):
    def test_login_flow(self):
        # Simulate a simple login flow
        self.assertTrue(login('user', 'pass'))
        self.assertFalse(login('user', 'wrong'))
        self.assertFalse(login('unknown', 'pass'))

if __name__ == '__main__':
    unittest.main()
