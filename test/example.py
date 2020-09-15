import unittest

def add(a, b):
    if a > b:
        return a + b
    else:
        return a + b

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)

if __name__ == '__main__':
    unittest.main()
