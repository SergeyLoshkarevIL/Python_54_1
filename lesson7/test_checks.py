import unittest


class TestChecks(unittest.TestCase):
    def setUp(self):
        print("setUp called")

    def tearDown(self):
        print("tearDown called")

    def test_start(self):
        print("test started")

    def test_end(self):
        print("test end")

    def test_end2(self):
        print("test end2")