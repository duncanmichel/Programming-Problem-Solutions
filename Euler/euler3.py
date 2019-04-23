"""

"""

#code
def isPrime(x):
    if x < 2: return False
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True
    
def createSieve(maxNum):
    if maxNum < 2: #no primes less than 2
        return 0
    nums = [1] * maxNum #identify 'prime'ness of nums up to maxNum
    nums[0] = nums[1] = 0 #not primes
    #print("sieve looks like",nums)
    for index in range(2, int(maxNum ** 0.5) + 1):#no prime factors after square root
        if nums[index] == 1:
            nums[index*index:maxNum:index] = [0] * int((maxNum-index*index-1)/index + 1)  
            nums[index] = index #put value at index
        #print("at index",index,"sieve looks like",nums)
    for index in range(int(maxNum ** 0.5) + 1,maxNum//2): #all numbers not marked '0' after square root are prime
        if nums[index] == 1:
            nums[index] = index #put value at index
    #print("At end sieve looks like",nums)
    return [x for x in nums if (x != 0 and x != 1)]

def largestPrimeFactor(num:int,nums):
    #if isPrime(num): # if num is prime, it will be the largest prime factor 
    #    return num 
    '''
    #not working, because taking too long
    for x in reversed(range(1,num//2+1,2)): #look down from half to 2
        #print(x)
        if num%x == 0 and isPrime(x):
            return x
    '''
    #print(nums)
    #not working, because memory error trying to allocate initial list for large values in createSieve() 
    for x in reversed(nums): #check list of primes less than number to see if they are factors, largest to smallest
        if num%x == 0: return x
    return num #num must be prime

if __name__ == "__main__":
    #print("I am main")
    n = 39
    #n = 600851475143
    print("The largest prime factor of ",n,"is",largestPrimeFactor(n,createSieve(n)))
