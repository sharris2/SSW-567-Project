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

def classifyTriangle(a,b,c):
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
    # require that the input values be > 0 and <= 200
    if a > 200 and b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
        
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
        
        
def runClassifyTriangle(a, b, c):
    """ invoke buggyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,b))    
    #print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,b),sep="")

# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests

    def testClassifyTriangleInvalid(self):
        # Tests for Invalid Input
        self.assertEqual(classifyTriangle(5,5,5.5),'InvalidInput','5,5,5.5 contains a side that is not an integer')
        self.assertEqual(classifyTriangle(5,5.5,5),'InvalidInput','5,5.5,5 contains a side that is not an integer')
        self.assertEqual(classifyTriangle(55.5,5,5),'InvalidInput''5.5,5,5 contains a side that is not an integer')
        self.assertEqual(classifyTriangle(3,4,0),'InvalidInput','3,4,0 contains a side less than or equal to 0')
        self.assertEqual(classifyTriangle(3,0,4),'InvalidInput','3,0,4 contains a side less than or equal to 0')
        self.assertEqual(classifyTriangle(0,3,4),'InvalidInput','0,3,4 contains a side less than or equal to 0')
        self.assertEqual(classifyTriangle(190,185,210),'InvalidInput','210,280,350 contains a side greater than 200')
        self.assertEqual(classifyTriangle(190,210,185),'InvalidInput','210,210,210 contains a side greater than 200')
        self.assertEqual(classifyTriangle(210,190,185),'InvalidInput','210,210,220 contains a side greater than 200')
        
    def testClassifyTriangleNot(self):
         # Test cases for Not A Triangle
        self.assertEqual(classifyTriangle(10,3,5),'NotATriangle','10,3,5 is Not A Triangle')
        self.assertEqual(classifyTriangle(3,10,5),'NotATriangle','3,10,5 is Not A Triangle')
        self.assertEqual(classifyTriangle(3,5,10),'NotATriangle','3,5,10 is Not A Triangle')

    def testClassifyTriangleEquilateral(self): # test invalid inputs
        # Test for Equilateral Trinagles
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 is an Equilateral Triangle')
        
    def testClassifyTriangleRight(self): 
        # Test for Right Triangles
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right Triangle')
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right Triangle')
        self.assertEqual(classifyTriangle(5,3,4),'Right','4,3,5 is a Right Triangle')
        
    def testClassifyTriangleScalene(self):
        # Test for Scalene Triangles
        self.assertEqual(classifyTriangle(10,11,12),'Scalene','10,11,12 is a Scalene Triangle')
        
    def testClassifyTriangleIsoceles(self):
        # Tests for Isoceles Triangles        
        self.assertEqual(classifyTriangle(6,6,8),'Isoceles','6,6,8 is an Isoceles Triangle')
        self.assertEqual(classifyTriangle(6,8,6),'Isoceles','6,8,6 is an Isoceles Triangle')
        self.assertEqual(classifyTriangle(8,6,6),'Isoceles','8,6,6 is an Isoceles Triangle')
        
if __name__ == '__main__':
    # examples of running the  code
    #runClassifyTriangle(1,2,3)
    #runClassifyTriangle(1,1,1)
    #runClassifyTriangle(3,4,5)
    
    print('Begin UnitTest')
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       