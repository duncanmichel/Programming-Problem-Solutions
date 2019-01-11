
"""
Problem Description
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        progression = []
        for i in range(1,n+1):
            if i % 15 == 0:
                progression.append("FizzBuzz")
            elif i % 3 == 0:
                progression.append("Fizz")
            elif i % 5== 0:
                progression.append("Buzz")
            else:
                progression.append(str(i))
        return progression

"""
Fastest Solution:
class Solution:
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
        
 Alternative:
 class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        mapping = {3: "Fizz", 5:"Buzz"}
        res = []
        
        for i in range(1, n+1):
            r = ""
            for key,value in mapping.items():
                if not i % key:
                    r+= value
            if r == "": 
                r = str(i)
            res.append(r)
        return res

"""
