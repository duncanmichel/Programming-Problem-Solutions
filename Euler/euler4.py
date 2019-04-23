"""
Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

#code
import math
#not used
def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def isPalindrome(x: int) -> bool:
    if x < 0: return False
    if x < 10: return True
    size = 0
    num = x
    while num > 0:
        size += 1
        num //= 10
    stack,middle,odd = [],size//2,True if size%2==1 else False
    #print('size',size,'middle',middle,'odd',odd)
    for i in range(size):
        if i < middle:
            stack.append(x%10)
        elif i == middle and odd:
            #print("got to odd condition on index",i,"x is ",x)
            pass
        else:
            if stack.pop() != x%10: return False
        x //= 10
    return True

def main():
    '''
    low = 100 * 100
    high = 999 * 999
    palindromes = []
    for num in range(low,high+1):
        if isPalindrome(num):
            palindromes.append(num)
    for num in reversed(palindromes):
        if isPrime(num):
            print(num,"is prime")
        else:
            pass #realized that checking by factor will be easier
    '''
    answer = 10
    min = 100
    for factor in reversed(range(100,1000)):
        if factor <= min:
            break
        for cofactor in reversed(range(100,1000)):
            if isPalindrome(factor * cofactor):
                answer = max(answer,factor * cofactor)
                min = max(min,cofactor)
                
    print(answer,"is the largest palindrome product of two three digit numbers")
    
if __name__ == "__main__":
    print("I am main")
    main()
else:
    print("I am not main")
    
