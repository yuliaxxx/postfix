import unittest
import calc

class Test(unittest.TestCase):

    def testS(self):
        exp = "2 4 9 - +".split()
        self.assertEquals(calc.calc(exp), 7)

    def testF(self):
        exp = "2 3 4 2 - + ".split()
        with self.assertRaises(TypeError): calc.calc(exp)

if __name__ == '__main__':
    unittest.main()