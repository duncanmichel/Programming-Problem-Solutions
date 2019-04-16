"""
Count the number of prime numbers less than a non-negative number, n.
Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution:
    def isPrime(x):
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return False
        return True
    
    def countPrimes(self, n: 'int') -> 'int':
        
        sieve = [False,False]
        count = 0
        num = 0
        coef = 1
        
        for x in range(2,n):
            sieve.append(True)
            
        for i in range(2,int(math.sqrt(n))+1):
            num = i
            coef = i
            if not sieve[i]:
                continue
            #print ("[DEBUG] prime found: "+str(i))
            num = i*coef
            while num < n:                
                sieve[num] = False
                #print ("[DEBUG] added "+str(num)+" to sieve")
                coef += 1
                num = i*coef
                
                
        for x in sieve:
            if x:
                count += 1
            
        return count

#Runtime: 784 ms, faster than 42.06% of Python3 online submissions for Count Primes.
#Memory Usage: 30.7 MB, less than 50.72% of Python3 online submissions for Count Primes.

#hashmap solution, which ironically is currently performing slower than an indexed array
class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrime(x):
            if x == 1: return False
            for i in range(2,int(math.sqrt(x))+1):
                if x%i == 0:
                    return False
            return True
        
        sieve = {x:True for x in range(2,n)}
        sieve[0],sieve[1],count,num,coef = False,False,0,0,1
            
        for i in range(2,int(math.sqrt(n))+1):
            num,coef = i*i,i
            if not sieve[i]:
                continue
            while num < n:                
                sieve[num] = False
                coef += 1
                num = i*coef   
                
        for x in sieve.keys():
            if sieve[x]:
                count += 1
            
        return count
"""
Runtime: 1580 ms, faster than 20.70% of Python3 online submissions for Count Primes.
Memory Usage: 221 MB, less than 5.46% of Python3 online submissions for Count Primes.
"""

"""
My Sieve of Erastothenes Solution:

class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        
        sieve = []
        count = 0
        num = 0
        coef = 1
        
        for x in range(2,n):
            num = x
            coef = x
            if x in sieve:
                continue
            else:
                count += 1
                #print ("[DEBUG] prime found: "+str(x))
                while num <= n:
                    sieve.append(num)
                    #print ("[DEBUG] added "+str(num)+" to sieve")
                    num = x*coef
                    coef += 1
        return count
"""

"""
Fastest Solution (116ms):
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i*i:n:i] = [0] * int((n-i*i-1)/i + 1)               
        return sum(s)
        
        return sum(p) - 2
"""
