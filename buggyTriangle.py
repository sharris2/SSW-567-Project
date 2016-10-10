# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available

def classify_triangle(a_value, b_value, c_value):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'


      BEWARE: there may be a bug or two in this code

    """
    classification = 'InvalidInput'
    # require that the input values be > 0 and <= 200
    # Changed "a > 200 and b > 200 or c > 200"
    #to "a > 200 or b > 200 or c > 200" after second test result.
    if a_value > 200 or b_value > 200 or c_value > 200:
        classification = 'InvalidInput'

    # Changed "b <= b" to "b <= 0" after first test result.
    elif a_value <= 0 or b_value <= 0 or c_value <= 0:
        classification = 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    elif (not(isinstance(a_value, (float, int)) and
            isinstance(b_value, (float, int)) and
            isinstance(c_value, (float, int)))):
        classification = 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    # Changed "(a >= (b - c)) or (b >= (a - c)) or (c >= (a + b))" to
    # "(a >= (b + c)) or (b >= (a + c)) or (c >= (a + b))" after test 2.
    elif ((a_value >= (b_value + c_value)) or (b_value >= (a_value + c_value))
            or (c_value >= (a_value + b_value))):
        classification = 'NotATriangle'

    # now we know that we have a valid triangle
    # Changed "b == a" to "b == c" after the third test result.
    elif a_value == b_value and b_value == c_value:
        classification = 'Equilateral'
    # Changed a*2 to a**2 for a,b,c after third test result,
    # added 2 other valid cases that were not checked.
    elif (calculate_relative_error(((a_value ** 2) + (b_value ** 2)), (c_value ** 2)) < 0.01 or
          calculate_relative_error(((a_value ** 2) + (c_value ** 2)), (b_value ** 2)) < 0.01 or
          calculate_relative_error(((b_value ** 2) + (c_value ** 2)), (a_value ** 2)) < 0.01):
        if (a_value != b_value) and  (b_value != c_value) and (a_value != c_value):
            classification = 'Right Scalene'
        elif (a_value == b_value) or (a_value == c_value) or (b_value == c_value):
            classification = 'Right Isoceles'
    # Changed last a!=b to a!=c after third test result.
    elif (a_value != b_value) and  (b_value != c_value) and (a_value != c_value):
        classification = 'Scalene'
    else:
        classification = 'Isoceles'
    
    return classification

def calculate_relative_error(value, actual):
    """Helper function to calculate the relative error"""
    #print (abs(float(actual) - float(value))/float(actual))
    return abs(float(actual) - float(value))/float(actual)

def run_classify_triangle(a_value, b_value, c_value):
    """ invoke buggyTriangle with the specified arguments and print the result """
    print('classify_triangle(', a_value, ',', b_value, ',', c_value, ')=',
          classify_triangle(a_value, b_value, c_value))
    #print('classify_triangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,b),sep="")

# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """ define multiple sets of tests as functions with names that begin
    with 'test'.  Each function may include multiple tests """

    def test_classify_triangle_invalid(self):
        """Tests for Invalid Input"""
        self.assertEqual(classify_triangle(5, 5, "a"), 'InvalidInput',
                         '5,5,a contains a side that is not a real number')
        self.assertEqual(classify_triangle(5, "a", 5), 'InvalidInput',
                         '5,a,5 contains a side that is not a real number')
        self.assertEqual(classify_triangle("a", 5, 5), 'InvalidInput',
                         'a,5,5 contains a side that is not a real number')
        self.assertEqual(classify_triangle(3, 4, 0), 'InvalidInput',
                         '3,4,0 contains a side less than or equal to 0')
        self.assertEqual(classify_triangle(3, 0, 4), 'InvalidInput',
                         '3,0,4 contains a side less than or equal to 0')
        self.assertEqual(classify_triangle(0, 3, 4), 'InvalidInput',
                         '0,3,4 contains a side less than or equal to 0')
        self.assertEqual(classify_triangle(190, 185, 210), 'InvalidInput',
                         '190,185,210 contains a side greater than 200')
        self.assertEqual(classify_triangle(190, 210, 185), 'InvalidInput',
                         '190,210,185 contains a side greater than 200')
        self.assertEqual(classify_triangle(210, 190, 185), 'InvalidInput',
                         '210,190,185 contains a side greater than 200')

    def test_classify_triangle_not(self):
        """Test cases for Not A Triangle"""
        self.assertEqual(classify_triangle(10, 3, 5), 'NotATriangle', '10,3,5 is Not A Triangle')
        self.assertEqual(classify_triangle(3, 10, 5), 'NotATriangle', '3,10,5 is Not A Triangle')
        self.assertEqual(classify_triangle(3, 5, 10), 'NotATriangle', '3,5,10 is Not A Triangle')

    def test_classify_triangle_equi(self): # test invalid inputs
        """Test for Equilateral Trinagles"""
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral',
                         '5,5,5 is an Equilateral Triangle')

    def test_classify_triangle_right(self):
        """Test for Right Triangles"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene',
                         '3,4,5 is a Right Scalene Triangle')
        self.assertEqual(classify_triangle(3, 5, 4), 'Right Scalene',
                         '3,5,4 is a Right Scalene Triangle')
        self.assertEqual(classify_triangle(5, 3, 4), 'Right Scalene',
                         '4,3,5 is a Right Scalene Triangle')
        self.assertEqual(classify_triangle(9.1, 9.1, 12.87), 'Right Isoceles',
                         '9.1, 9.1, 12.87 is a Right Isoceles Triangle')
        self.assertEqual(classify_triangle(9.1, 12.87, 9.1), 'Right Isoceles',
                         '9.1, 12.87, 9.1 is a Right Isoceles Triangle')
        self.assertEqual(classify_triangle(12.87, 9.1, 9.1), 'Right Isoceles',
                         '12.87,9.1,9.1 is a Right Isoceles Triangle')

    def test_classify_triangle_scalene(self):
        """Test for Scalene Triangles"""
        self.assertEqual(classify_triangle(10, 11, 12), 'Scalene',
                         '10,11,12 is a Scalene Triangle')

    def test_classify_triangle_isoceles(self):
        """Tests for Isoceles Triangles"""
        self.assertEqual(classify_triangle(6, 6, 8), 'Isoceles',
                         '6,6,8 is an Isoceles Triangle')
        self.assertEqual(classify_triangle(6, 8, 6), 'Isoceles',
                         '6,8,6 is an Isoceles Triangle')
        self.assertEqual(classify_triangle(8, 6, 6), 'Isoceles',
                         '8,6,6 is an Isoceles Triangle')
        self.assertEqual(classify_triangle(10, 12, 10), 'Isoceles',
                         '10,12,10 is an Isoceles Triangle')

if __name__ == '__main__':
    print (classify_triangle(5, 5, 5.5), 'InvalidInput',
           '5,5,5.5 contains a side that is not an integer')
    print (classify_triangle(5, 5.5, 5), 'InvalidInput',
           '5,5.5,5 contains a side that is not an integer')
    print (classify_triangle(5.5, 5, 5), 'InvalidInput',
           '5.5,5,5 contains a side that is not an integer')
    print (classify_triangle(3, 4, 0), 'InvalidInput',
           '3,4,0 contains a side less than or equal to 0')
    print (classify_triangle(3, 0, 4), 'InvalidInput',
           '3,0,4 contains a side less than or equal to 0')
    print (classify_triangle(0, 3, 4), 'InvalidInput',
           '0,3,4 contains a side less than or equal to 0')
    print (classify_triangle(190, 185, 210), 'InvalidInput',
           '190,185,210 contains a side greater than 200')
    print (classify_triangle(190, 210, 185), 'InvalidInput',
           '190,210,185 contains a side greater than 200')
    print (classify_triangle(210, 190, 185), 'InvalidInput',
           '210,190,185 contains a side greater than 200')

    # Test cases for Not A Triangle
    print classify_triangle(10, 3, 5), 'NotATriangle', '10,3,5 is Not A Triangle'
    print classify_triangle(3, 10, 5), 'NotATriangle', '3,10,5 is Not A Triangle'
    print classify_triangle(3, 5, 10), 'NotATriangle', '3,5,10 is Not A Triangle'

    # Test for Equilateral Trinagles
    print classify_triangle(5, 5, 5), ': Equilateral', '5,5,5 is an Equilateral Triangle'

    # Test for Right Triangles
    print classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right Scalene Triangle'
    print classify_triangle(3, 5, 4), 'Right', '3,5,4 is a Right Scalene Triangle'
    print classify_triangle(5, 3, 4), 'Right', '4,3,5 is a Right Scalene Triangle'

    # Test for Scalene Triangles
    print classify_triangle(10, 11, 12), 'Scalene', '10,11,12 is a Scalene Triangle'

    # Tests for Isoceles Triangles
    print classify_triangle(6, 6, 8), 'Isoceles', '6,6,8 is an Isoceles Triangle'
    print classify_triangle(6, 8, 6), 'Isoceles', '6,8,6 is an Isoceles Triangle'
    print classify_triangle(8, 6, 6), 'Isoceles', '8,6,6 is an Isoceles Triangle'
    print classify_triangle(10, 12, 10), 'Isoceles', '10,12,10 is an Isoceles Triangle'
    print 'Begin UnitTest'
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True)
    # this runs all of the tests - use this line if running from the command line
