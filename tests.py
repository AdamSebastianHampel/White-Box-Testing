import unittest
from contrived_func import contrived_func

class TestCase(unittest.TestCase):

    def test1(self):
        # F, F, T, F

        val = 1
        self.assertGreater(contrived_func(val), 0)

    def test2(self):
        # F, F, T, T

        val = -1
        self.assertGreater(contrived_func(val), 0)

    def test3(self):
        # F, T, T, F

        val = 0
        self.assertGreater(contrived_func(val), 0)

    def test4(self):
        # F, T, T, T

        val = -2
        self.assertGreater(contrived_func(val), 0)

    def test5(self):
        # T, F, F, F

        val = 21
        self.assertGreater(contrived_func(val), 0)

    def test6(self):
        # T, F, T, F

        val = 19
        self.assertGreater(contrived_func(val), 0)

    def test7(self):
        # T, T, F, F

        val = 50
        self.assertGreater(contrived_func(val), 0)

    def test8(self):
        # T, T, T, F

        val = 18
        self.assertGreater(contrived_func(val), 0)

if __name__ == '__main__':
    unittest.main()

