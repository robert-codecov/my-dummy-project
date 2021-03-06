import unittest

from extra import line

def div(a, b):
    if a == None:
        raise Exception("a must be defined")

    if b == None:
        raise Exception("b must be defined")
    
    if b == 0:
        return None
    else:
        return a / b

def mult(a, b):
    if a == None:
        raise Exception("a must be defined")

    if b == None:
        raise Exception("b must be defined")

    return a * b

def sub(a, b):
    if a == None:
        raise Exception("a must be defined")

    if b == None:
        raise Exception("b must be defined")

    return a - b

def add(a, b):
    if a == None:
        raise Exception("a must be defined")

    if b == None:
        raise Exception("b must be defined")

    if a > b:
        return a + b
    else:
        return a + b

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)

    def test_mult(self):
        self.assertEqual(mult(2, 3), 6)

    def test_line(self):
        self.assertEqual(line(1, 1, 1), 2)

if __name__ == '__main__':
    unittest.main()

