import unittest
import mymath

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)
    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mymath.subtract(10.5, 2)
        self.assertEqual(result, 8.5)
    def test_add_mulanddiv(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mymath.multiply(5, 3)
        self.assertEqual(result, 15)
        
        result = mymath.divide(6, 3)
        self.assertEqual(result, 2.0)
if __name__ == '__main__':
    unittest.main()