"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

#code
def sumPrimes(maxNum):
    if maxNum < 2: #no primes less than 2
        return 0
    nums = [1] * maxNum #identify 'prime'ness of nums up to maxNum
    nums[0] = nums[1] = 0 #not primes
    for index in range(2, int(maxNum ** 0.5) + 1):#no prime factors after square root
        if nums[index] == 1:
            nums[index*index:maxNum:index] = [0] * int((maxNum-index*index-1)/index + 1)  
            nums[index] = index #put value at index
    for index in range(int(maxNum ** 0.5) + 1,maxNum): #all numbers not marked '0' after square root are prime
        if nums[index] == 1:
            nums[index] = index #put value at index
    #print(nums)
    return sum(nums) #sum all numbers in array because non-primes are zero

if __name__ == "__main__":
    #print("I am main")
    n = 2000000
    print("sum of primes less than",n,"is",sumPrimes(n))
