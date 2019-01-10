"""
Bubble Sort
Complexity: 
The complexity of bubble sort is O(n**2) in both worst and average cases, because the entire array needs to be iterated for every element.

You have been given an array A of size N . you need to sort this array non-decreasing oder using bubble sort. However, you do not 
need to print the sorted array . You just need to print the number of swaps required to sort this array using bubble sort
Input Format
The first line consists of a single integer N denoting size of the array. The next line contains N space separated integers denoting 
the elements of the array.
Output Format 
Print the required answer in a single line
"""
size = int(input())
numlist = list(map(int,input().split()))
numswaps = 0
temp = 0
swap = True

for i in range(0,size-1):
    if not swap:
        break
    swap = False
    for j in range(0,size-1):
        if numlist[j] > numlist[j+1]:
            temp = numlist[j]
            numlist[j] = numlist[j+1]
            numlist[j+1] = temp
            numswaps += 1
            swap = True
print(numswaps)


