from unittest import TestCase

from lesson6 import calculator


class TestCalculator(TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)


#AssertEqual(a,b)
#AssertEqual(2+2,4)

#AssertTrue(a)
#def is_even(num):
    #return num % 2 == 0
#self.assertTrue(is_even(4))

#AssertFalse(e)
#self.assertFalse(is_even(9))

#assertRaises
def divide(a,b):
    if b ==0:
        raise ValueError("Division by zero")
    return a/b