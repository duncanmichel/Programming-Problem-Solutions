"""
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
