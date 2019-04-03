"""
Reservoir Sampling Problem (select a random number from a stream of numbers with 1/n probability
"""
 
import random 

# The resultant random number 
res = 0; 
  
# A function to randomly select a item from stream[0], stream[1], .. stream[i-1] 
def selectRandom(x,count,res): 
    # increment count of numbers seen so far 
    count += 1; 
  
    # If this is the first element from stream, return it 
    if (count == 1): 
        res = x; 
    else: 
          
        # Generate a random number from 0 to count - 1 
        i = random.randrange(count); 
  
        # Replace the prev random number with new number with 1/count probability 
        if (i == count - 1): 
            res = x; 
    return res; 
  
# Test Code 
stream = [1, 2, 3, 4]; 
n = len(stream); 

for i in range (n): 
    res = selectRandom(stream[i],i,res)
    print("Random number from first",  i+1 , "numbers is", res);
