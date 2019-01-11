"""
Linear Search
Print a single integer denoting the index of the last occurrence of integer M in the array if it exists, otherwise print -1.
Sample Input
5 1
1 2 3 4 1

Sample Output
4
"""

[size, num] = map(int,input().split())
numlist = map(int,input().split())
count = -1
last = -1
for i in numlist:
    count += 1
    if i == num:
        last = count
        
print(last)

"""
Binary Search
**works only on a sorted set
Input Format
The first line consists of a single integer N denoting the size of array A. The next line contains N unique integers, 
denoting the content of array A. The next line contains a single integer q denoting the number of queries. Each of the 
next q lines contains a single integer x denoting the element whose rank based position needs to be printed.
Output Format
You need to print q integers denoting the answer to each query.

Sample Input
5
1 2 3 4 5
5
1
2
3
4
5

Sample Output
1
2
3
4
5
"""
def binsearch(tgt,ub,lb,nlist):
    mp = int((lb+ub)/2)
    #print("[DEBUG:binsearch] Midpoint " + str(mp) + " of list [" + str(lb) + ":" + str(ub) + "]")
    if nlist[mp] < tgt:
        return binsearch(tgt,ub,mp+1,nlist)
    elif nlist[mp] > tgt:
        return binsearch(tgt,mp,lb,nlist)
    else:
        return mp

size = int(input())
numlist = list(map(int,input().split()))
if numlist[0] > numlist[1]: # check for sorted data
    numlist.sort()
numquery = int(input())
lb = 0 #lower bound
ub = size #upper bound
mp = (lb+ub)/2 #midpoint


while (numquery > 0):
    query = int(input())
    #print("[DEBUG:main] Current query: " + str(query))
    if (query >= numlist[0]) and (query <= numlist[size-1]):
        print(binsearch(query,size-1,0,numlist)+1)
    else:
        print(-1)
    numquery -= 1

    
"""
Ternary Search (incomplete)
You have been given an Unimodal function: 
 f(x) = 2x^2 -12x + 7 
with N intervals. For each interval you will be given two integer values l and r , where l \le r and you need to find the minimum value of f(x) where x will be in the range [l,r] (both inclusive).

Input:
The first line will consists of one integer N denoting the number of intervals. 
In next N lines, each line contains 2 space separated integers, l and r denoting the range of interval.

Output:
Print N lines, where i_{th} line denotes the minimum value of f(x), where x will be in range [l_i, r_i] 
"""
def func(x=0):
    return 2*x*x + -12*x +7; #unimodal function


n = int(input())
for i in range(0,n):
    [l,r] = map(int,input().split())
    for j in range(0,200):
        mid1 = int((l*2+r)/3)
        mid2 = int((l+2*r)/3)
        if(func(mid1) < func(mid2)):
            r = mid2
        else: 
            l = mid1
    print(func(l)) 
