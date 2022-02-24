"""
Functions that compute square roots of numbers in a list.
Test to confirm that your function works correctly.
"""
import math
import unittest

values1 = [1, 4, 3.14, 0, 0.001]
values2 = [0, -1, -2]
values3 = [4, 25]

def root(self,values):
    #This function calculates roots using the math lib
    roots = []
    for i in values:
     roots.append(math.sqrt(i))
    return roots

def manualroot(values):
    #This function is the same as above but without using te math lib
    roots = []
    for i in values:
        roots.append(i ** 0.5)
    return roots





class testsqrt(unittest.TestCase):
    def testRoot(self):
        self.assertEqual(root(self,[25,4]), [5,2])
        print("Success")

if __name__ == '__main__':
    unittest.main()