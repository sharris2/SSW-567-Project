import unittest

def classifyTriangle(a, b, c):
    string = ""

    #checking if it is scalene, isosceles, or equilateral
    if a == b or b == c:
        if c == a:
            string = "The triangle is equilateral."
        else:
            string = "The triangle is isosceles."
    else:
        string = "The triangle is scalene."

    if (a**2 + b**2) == c**2:
        string += " It is also a right triangle."
        
    #print string
    return string


class TestClassifyTriangle(unittest.TestCase):

    def test_scalene(self):
        x = classifyTriangle(1,2,3)
        self.assertEqual("The triangle is scalene.", x)
        
    def test_right_scalene(self):
        x = classifyTriangle(3,4,5)
        self.assertEqual("The triangle is scalene. It is also a right triangle.", x)

    def test_isosceles(self):
        x = classifyTriangle(3,3,4)
        self.assertEqual("The triangle is isosceles.", x)

    def test_equ(self):
        x = classifyTriangle(3,3,3)
        self.assertEqual("The triangle is equilateral.", x)

    # This test will fail, but we wanted to show that we understood the tool.
    # We would need to fix the if statement which checks for a right triangle
    def test_right_triangle(self):
        x = classifyTriangle(6,10,8)
        self.assertEqual("The triangle is scalene. It is also a right triangle.", x)

if __name__ == '__main__':
    print classifyTriangle(11,11,29)
    print classifyTriangle(10,8,13)
    print classifyTriangle(7,7,7)
    print classifyTriangle(20,50,40)
    print classifyTriangle(9,12,15)
    unittest.main()


    
