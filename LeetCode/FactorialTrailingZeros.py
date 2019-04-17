"""
Given an integer n, return the number of trailing zeroes in n!.
Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
https://leetcode.com/problems/factorial-trailing-zeroes/submissions/
"""
#https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52371/My-one-line-solutions-in-3-languages
#https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52399/My-python-solution-in-O(1)-space-O(logN)-time

#Algorithmically accurate, but too slow
class Solution:
    def trailingZeroes(self, n: int) -> int:
        tens,fives,twos = 0,0,0
        while n > 1:
            if n%10==0: 
                temp = n
                while temp%10 == 0:
                    tens += 1
                    temp //= 10
                while temp%5 == 0:
                    fives += 1
                    temp //= 5
                n-= 5                
            elif n%5 == 0:
                temp = n
                while temp%5 == 0:
                    fives += 1
                    temp //= 5
                n-= 5
            else:
                n -= 1
        #print("tens",tens,"fives",fives)
        return tens + fives

"""
#memoization solution, not working yet
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num,tens,fives,count = 2,0,0,0
        memo = {}
        while num <= n:
            temp = num
            print("checking",num,"", end='')
            if num%10==0: 
                check = True
                count = 0
                while temp%10 == 0:
                    if temp in memo:
                        print("memo check in tens",temp)
                        tens += 1 + memo[temp][0]
                        #fives += memo[temp][1] ???
                        count = 0
                        check = False
                        break
                    count += 1
                    #tens += 1
                    temp //= 10
                tens += count
                while check and temp%5 == 0:
                    fives += 1
                    temp //= 5
                memo[num] = (tens, fives)
                num += 5                
            elif num%5 == 0:
                count = 0
                while temp%5 == 0:
                    if temp in memo:
                        print("memo check in fives",temp)
                        fives += 1 + memo[temp][1]
                        count = 0
                        break
                    count += 1
                    #fives += 1
                    temp //= 5
                fives += count
                memo[num] = (tens, fives)
                num += 5
            else:
                num += 1
            print("tens",tens,"fives",fives)
        #print("tens",tens,"fives",fives)
        return tens+fives
        

1808548329
7392

checking 2 tens 0 fives 0
checking 3 tens 0 fives 0
checking 4 tens 0 fives 0
checking 5 tens 0 fives 1
checking 10 tens 1 fives 1
checking 15 tens 1 fives 2
checking 20 tens 2 fives 2
checking 25 memo check in fives 5
tens 2 fives 4
checking 30 tens 3 fives 4
checking 35 tens 3 fives 5
checking 40 tens 4 fives 5
checking 45 tens 4 fives 6
checking 50 tens 5 fives 7
checking 55 tens 5 fives 8
checking 60 tens 6 fives 8
checking 65 tens 6 fives 9
checking 70 tens 7 fives 9
checking 75 memo check in fives 15
tens 7 fives 12
checking 80 tens 8 fives 12
checking 85 tens 8 fives 13
checking 90 tens 9 fives 13
checking 95 tens 9 fives 14
checking 100 memo check in tens 10
tens 11 fives 14

checking 2 tens 0 fives 0
checking 3 tens 0 fives 0
checking 4 tens 0 fives 0
checking 5 tens 0 fives 1
checking 10 tens 1 fives 1
checking 15 tens 1 fives 2
checking 20 tens 2 fives 2
checking 25 memo check in fives 5
tens 2 fives 3
checking 30 tens 3 fives 3
checking 35 tens 3 fives 4
checking 40 tens 4 fives 4
checking 45 tens 4 fives 5
checking 50 tens 5 fives 6
checking 55 tens 5 fives 7
checking 60 tens 6 fives 7
checking 65 tens 6 fives 8
checking 70 tens 7 fives 8
checking 75 memo check in fives 15
tens 7 fives 10
checking 80 tens 8 fives 10
checking 85 tens 8 fives 11
checking 90 tens 9 fives 11
checking 95 tens 9 fives 12
checking 100 memo check in tens 10
tens 10 fives 12

checking 2 tens 0 fives 0
checking 3 tens 0 fives 0
checking 4 tens 0 fives 0
checking 5 tens 0 fives 1
checking 10 tens 1 fives 1
checking 15 tens 1 fives 2
checking 20 tens 2 fives 2
checking 25 tens 2 fives 4
checking 30 tens 3 fives 4
checking 35 tens 3 fives 5
checking 40 tens 4 fives 5
checking 45 tens 4 fives 6
checking 50 tens 5 fives 7
checking 55 tens 5 fives 8
checking 60 tens 6 fives 8
checking 65 tens 6 fives 9
checking 70 tens 7 fives 9
checking 75 tens 7 fives 11
checking 80 tens 8 fives 11
checking 85 tens 8 fives 12
checking 90 tens 9 fives 12
checking 95 tens 9 fives 13
checking 100 tens 11 fives 13
"""
    
"""
My Solution:

"""

"""
Fastest Solution ():


Smallest Memory ():

"""
