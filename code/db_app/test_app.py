import unittest
from app import connect_and_test_db


class TestApp(unittest.TestCase):
    def test_db_connection(self):
        self.assertTrue(connect_and_test_db())


if __name__ == '__main__':
    unittest.main()
