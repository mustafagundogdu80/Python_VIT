"""
Inheritance: https://www.hackerrank.com/challenges/inheritance/problem
"""
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName,lastName,idNum)
        self.scores = scores
        
    def calculate(self):
        grade_sum = 0
        for i in self.scores:
            grade_sum += i
        avarage_grade = grade_sum / len(self.scores)
        if 100>= avarage_grade >= 90 :
            return "O"
        elif 90 > avarage_grade >= 80:
            return "E"
        elif 80 > avarage_grade >= 70:
            return "A"
        elif 70 > avarage_grade >= 55:
            return "P"
        elif 55 > avarage_grade >= 40:
            return "D"
        else:
            return "T"
            
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
"""--------------------------------------------------------------------"""

"""
Classes: Dealing with Complex Numbers: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
"""
# import math

# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
#     def __add__(self, no):
#         #(a + bi)+(c + di) = (a+c) +(b+d)i
#         return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
#     def __sub__(self, no):
#         #(a+bi)-(c+di)=(a-c)+(b-d)i
#         return Complex(self.real-no.real, self.imaginary - no.imaginary)
#     def __mul__(self, no):
#         #(a + bi) x (c + di) = (ac - bd)+(ad + bc)i
#         return Complex((self.real * no.real) - (self.imaginary * no.imaginary), (self.real * no.imaginary)+(self.imaginary* no.real) )

#     def __truediv__(self, no):
#         # (a + bi)/ (c + di) = ((ac+bd)/(c**2 + d**2))+((bc-ad)/(c**2 + d**2))
#         return Complex(((self.real*no.real)+(self.imaginary * no.imaginary))/(no.real **2 + no.imaginary **2),((self.imaginary * no.real) - (self.real * no.imaginary))/(no.real**2 + no.imaginary**2))

#     def mod(self):
#          # (a**2 + b**2)**0,5
#         return Complex(math.sqrt(self.real**2 + self.imaginary**2),0)

#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')